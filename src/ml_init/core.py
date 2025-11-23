from rich.console import Console
from .generator import ProjectGenerator
from .integrations import Integrations
from .presets import PresetsManager

console = Console()

def generate_project(config):
    """Orchestrates the project generation process."""
    name = config['name']
    console.print(f"[bold blue]Starting generation for project: {name}[/bold blue]")

    # 1. Generate Structure and Files
    generator = ProjectGenerator(config)
    generator.generate()

    # 2. Initialize Integrations
    integrations = Integrations(generator.path)
    
    # Git
    if "git" in config.get('integrations', []):
        integrations.init_git()

    # Poetry / Dependency Management
    if "poetry" in config.get('integrations', []):
        integrations.init_poetry(name, config.get('dependencies'))
    
    # DVC
    if "dvc" in config.get('integrations', []):
        integrations.init_dvc()

    console.print(f"\n[bold green]Project {name} created successfully![/bold green]")
    console.print(f"cd {name}")
    if "poetry" in config.get('integrations', []):
        console.print("poetry install")
        console.print("poetry run python src/train.py")
