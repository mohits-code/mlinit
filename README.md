# mlinit 🚀

[![PyPI version](https://badge.fury.io/py/mlinit.svg)](https://badge.fury.io/py/mlinit)
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

You can install `mlinit` directly from PyPI:

```bash
pip install mlinit
```

> **Tip**: If the `mlinit` command is not found after installation, run it via python:
> ```bash
> python -m mlinit.cli init --name my_project
> ```

## 🚀 Quick Start

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
