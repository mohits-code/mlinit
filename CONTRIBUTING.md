# Contributing to mlinit

We love your input! We want to make contributing to `mlinit` as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Setup

`mlinit` is built with Python. We recommend using a virtual environment for development.

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/mlinit.git
cd mlinit
```

### 2. Install Dependencies
You can install the package in editable mode with all dependencies:

```bash
pip install -e .
```

### 3. Run Tests
(Tests are currently being added, but you can run the CLI manually to verify changes)

```bash
python -m mlinit.cli init --name test_project
```

## Project Structure

- **`mlinit/`**: Source code.
    - **`cli.py`**: CLI entry point.
    - **`core.py`**: Orchestration logic.
    - **`generator.py`**: File generation and templating.
    - **`presets.py`**: Preset management.
    - **`integrations.py`**: Git/Poetry/DVC wrappers.
- **`mlinit/templates/`**: Jinja2 templates for generated files.

## Pull Request Process

1.  Fork the repo and create your branch from `main`.
2.  If you've added code that should be tested, add tests.
3.  Ensure the test suite passes.
4.  Make sure your code lints.
5.  Issue that pull request!

## Any questions?

Feel free to open an issue to discuss your ideas before diving in!
