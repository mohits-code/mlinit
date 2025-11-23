import os
from pathlib import Path
from ruamel.yaml import YAML

yaml = YAML()

PRESETS_DIR = Path.home() / ".mlinit" / "presets"

class PresetsManager:
    def __init__(self):
        self.presets_dir = PRESETS_DIR
        self.presets_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_default_presets()

    def _ensure_default_presets(self):
        """Create default presets if they don't exist."""
        default_preset = {
            "description": "Default ML project structure with Hydra",
            "dependencies": ["hydra-core", "omegaconf", "numpy", "pandas"],
            "integrations": ["git", "poetry"],
            "structure": {
                "conf/base": [],
                "data": ["raw", "processed", "external"],
                "src": ["models", "data", "utils"],
                "notebooks": [],
                "tests": [],
                "artifacts": []
            }
        }
        
        if not (self.presets_dir / "default.yaml").exists():
            self.save("default", default_preset)

        # CV Preset
        cv_preset = default_preset.copy()
        cv_preset["description"] = "Computer Vision project with PyTorch and Torchvision"
        cv_preset["dependencies"] = ["hydra-core", "omegaconf", "numpy", "pandas", "torch", "torchvision", "opencv-python"]
        if not (self.presets_dir / "cv.yaml").exists():
            self.save("cv", cv_preset)

        # NLP Preset
        nlp_preset = default_preset.copy()
        nlp_preset["description"] = "NLP project with Hugging Face Transformers"
        nlp_preset["dependencies"] = ["hydra-core", "omegaconf", "numpy", "pandas", "torch", "transformers", "datasets", "tokenizers"]
        if not (self.presets_dir / "nlp.yaml").exists():
            self.save("nlp", nlp_preset)

    def list(self):
        """List available presets."""
        return [f.stem for f in self.presets_dir.glob("*.yaml")]

    def load(self, name):
        """Load a preset by name."""
        preset_path = self.presets_dir / f"{name}.yaml"
        if not preset_path.exists():
            raise FileNotFoundError(f"Preset '{name}' not found.")
        
        with open(preset_path, "r") as f:
            return yaml.load(f)

    def save(self, name, config):
        """Save a configuration as a preset."""
        preset_path = self.presets_dir / f"{name}.yaml"
        with open(preset_path, "w") as f:
            yaml.dump(config, f)
