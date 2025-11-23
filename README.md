# mlinit 🚀

[![PyPI version](https://badge.fury.io/py/mlinit-cli.svg)](https://badge.fury.io/py/mlinit-cli)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**The production-ready scaffolder for Machine Learning projects.**

`mlinit` is a CLI tool designed to bootstrap Machine Learning projects with industry-standard best practices. It goes beyond simple directory creation by setting up a complete development environment with **Poetry**, **Hydra**, **Git**, and **CI/CD** out of the box.

---

## 💡 Why mlinit?

There are many scaffolders out there. Here is why `mlinit` is different:

| Feature | Cookiecutter | Kedro | **mlinit** |
| :--- | :--- | :--- | :--- |
| **Philosophy** | Generic templating engine | Full-fledged framework | **Lightweight scaffolder + Modern Stack** |
| **Config** | Static JSON | Custom ConfigLoader | **Hydra (Composable & Dynamic)** |
| **Deps** | `requirements.txt` usually | `pip-tools` | **Poetry (Native Integration)** |
| **Learning Curve** | Low | High | **Low (It's just a folder structure)** |

`mlinit` gives you the **structure** of a framework without forcing you to learn a new API. It sets up the tools you already love (Hydra, Poetry, PyTorch) so you can just write code.

## ✨ Features

*   **🏗 Production-Grade Structure**: Generates a robust directory layout optimized for reproducibility (separating data, source, configs, and artifacts).
*   **🐍 Modern Dependency Management**: Automatically initializes [Poetry](https://python-poetry.org/) projects, solving dependency hell before it starts.
*   **⚙️ Hydra Configuration**: Pre-configured [Hydra](https://hydra.cc/) setup for flexible, composable experiment configuration.
*   **💾 Smart Presets**: Built-in configurations for **Computer Vision**, **NLP**, and **General ML**. Save your own custom setups for future use.
*   **✅ CI/CD Ready**: Auto-generates GitHub Actions workflows to run your tests on every push.
*   **🔧 Git Integration**: Initializes a Git repository with a smart `.gitignore` tailored for ML (ignoring large data/artifacts).
*   **📄 Auto-Documentation**: Generates `README.md` files in every subdirectory explaining exactly what should go where.

## 📦 Installation

You can install the CLI package from PyPI (package name: `mlinit-cli`):

```bash
pip install mlinit-cli
```

> **Tip**: If the `mlinit` command is not found after installation, run it via python:
> ```bash
> python -m mlinit.cli init --name my_project
> ```

**CLI Usage — Cross‑platform**

We aim for instructions that work for everyone. Below are cross-platform options to install and run `mlinit` reliably.

- Recommended (best experience): install with `pipx` so the CLI is globally available and isolated:

```bash
python -m pip install --user pipx
python -m pipx ensurepath
pipx install mlinit-cli
```

- Virtual environment (per-project): create a venv and install the package there:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell (Windows)
source .venv/bin/activate        # bash/zsh (macOS/Linux)
pip install mlinit-cli
```

- Fallback (no PATH changes): run the CLI via Python module entry point anywhere:

```bash
python -m ml_init.cli init --name my_project
```

- Troubleshooting PATH issues

    - Windows (common): pip installs user scripts to a directory like:

        `C:\Users\<your-user>\AppData\Local\Packages\PythonSoftwareFoundation.Python.<ver>_qbz5n2kfra8p0\LocalCache\local-packages\Python<ver>\Scripts`

        To add it temporarily in PowerShell:

        ```powershell
        $env:Path += ';C:\Users\<your-user>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts'
        ```

        To add it permanently (replace `<your-user>` and then restart PowerShell):

        ```powershell
        $scriptPath = 'C:\Users\<your-user>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts'
        setx PATH "$($env:Path);$scriptPath"
        ```

    - macOS / Linux: pip typically installs user scripts to `~/.local/bin`. Add that to your shell profile if it's not already on PATH:

        ```bash
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.profile
        source ~/.profile
        ```

- Verify where the CLI was installed

```bash
python -m pip show mlinit-cli
python -m site --user-base   # shows base; scripts live in <base>/Scripts (Windows) or <base>/bin (Linux/macOS)
ls "$(python -m site --user-base)/bin"   # macOS/Linux
Get-ChildItem "$(python -m site --user-base)\Scripts"   # PowerShell
```

If you still see `mlinit` not found, use the `python -m` fallback above or install via `pipx` to avoid PATH issues entirely.

## 🚀 Quick Start

Check available commands or get help:

```bash
mlinit help
```

Initialize a new project in seconds:

```bash
mlinit init --name my_awesome_project
```

### Example Output
The tool generates a ready-to-run `train.py` integrated with Hydra:

```python
# src/train.py
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="../conf", config_name="config")
def train(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))
    # Your training logic here...
```

## 🛣️ Roadmap

- [ ] **MLflow Integration**: Auto-configure MLflow for experiment tracking.
- [ ] **DVC Setup**: Automated data version control hooks.
- [ ] **Cloud Deployment**: Terraform templates for AWS/GCP.
- [ ] **Streamlit/Gradio**: One-click demo app generation.

## 📂 The "mlinit" Standard Structure

Your generated project will look like this:

```text
my_project/
├── conf/                   # Hydra configuration files
│   ├── base/               # Base configs (train.yaml, model.yaml)
│   └── config.yaml         # Main entry point
├── data/                   # Data directory (gitignored content)
│   ├── raw/                # Immutable raw data
│   ├── processed/          # Canonical data sets for modeling
│   └── external/           # Data from third party sources
├── src/                    # Source code
│   ├── data/               # Scripts to generate data
│   ├── models/             # Model architectures
│   ├── utils/              # Helper functions
│   └── train.py            # Main training script (Hydra-enabled)
├── notebooks/              # Jupyter notebooks for exploration
├── tests/                  # Unit tests
├── artifacts/              # Model checkpoints, logs, outputs (gitignored)
├── .github/workflows/      # CI/CD pipelines (GitHub Actions)
├── pyproject.toml          # Project dependencies (Poetry)
├── README.md               # Project documentation
└── .gitignore              # Git ignore rules
```

## 🙏 Acknowledgements

This project was heavily inspired by [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science) project. We aim to bring that same spirit of community-driven standardization to the modern ML stack (Hydra, Poetry, etc.).

We believe in the power of the open-source community to build better tools together. If you have ideas or feedback, please open an issue!

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions.

1.  Fork the repository.
2.  Create a feature branch.
3.  Submit a Pull Request.

---

*Built with ❤️ for the ML Community.*
