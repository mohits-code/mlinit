import os
from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape
from rich.console import Console

console = Console()

class ProjectGenerator:
    def __init__(self, config):
        self.config = config
        self.name = config['name']
        self.path = Path.cwd() / self.name
        self.env = Environment(
            loader=PackageLoader("mlinit", "templates"),
            autoescape=select_autoescape()
        )

    def generate(self):
        """Main generation flow."""
        self.create_structure()
        self.render_templates()
        self.save_config()

    def save_config(self):
        """Saves the configuration used for generation."""
        from ruamel.yaml import YAML
        yaml = YAML()
        config_path = self.path / ".mlinit-config.yaml"
        with open(config_path, "w") as f:
            yaml.dump(self.config, f)


    def create_structure(self):
        """Creates the directory structure."""
        console.print(f"Creating project structure at [bold]{self.path}[/bold]...")
        
        # Base directories from config or default
        structure = self.config.get('structure', {})
        
        # Flatten structure for creation
        dirs_to_create = []
        for parent, children in structure.items():
            if not children:
                dirs_to_create.append(parent)
            else:
                for child in children:
                    dirs_to_create.append(f"{parent}/{child}")
        
        # Add standard dirs if not present
        standard_dirs = ["conf", "src", "tests", "artifacts", ".github/workflows"]
        for d in standard_dirs:
            if d not in dirs_to_create:
                dirs_to_create.append(d)

        for d in dirs_to_create:
            dir_path = self.path / d
            dir_path.mkdir(parents=True, exist_ok=True)
            (dir_path / ".gitkeep").touch()
        
        # Create src/__init__.py
        (self.path / "src" / "__init__.py").touch()

    def render_templates(self):
        """Renders and writes files from templates."""
        console.print("Rendering templates...")
        
        templates_map = {
            "README.md.j2": "README.md",
            "train.py.j2": "src/train.py",
            "ci.yml.j2": ".github/workflows/ci.yml",
        }
        
        for template_name, output_name in templates_map.items():
            template = self.env.get_template(template_name)
            content = template.render(config=self.config)
            
            output_path = self.path / output_name
            with open(output_path, "w") as f:
                f.write(content)
        
        # Write Hydra configs (static for now, could be templated)
        self._write_hydra_configs()

    def _write_hydra_configs(self):
        """Writes default Hydra configurations."""
        conf_path = self.path / "conf"
        (conf_path / "config.yaml").write_text("""
defaults:
  - _self_
  - base: train

hydra:
  run:
    dir: artifacts/outputs/${now:%Y-%m-%d}/${now:%H-%M-%S}
""")
        
        base_path = conf_path / "base"
        base_path.mkdir(exist_ok=True)
        (base_path / "train.yaml").write_text("""
epochs: 10
batch_size: 32
lr: 0.001
""")
