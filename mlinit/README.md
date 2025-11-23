# mlinit Source Documentation

## Architecture Overview

The package is organized into modular components to separate concerns between the CLI, logic, and external integrations.

### Core Components

*   **`cli.py`**: The entry point for the command-line interface.
    *   Uses `click` to define commands (`init`, `presets`).
    *   Handles argument parsing and user interaction.
    *   Delegates actual work to `core.py` and `presets.py`.

*   **`core.py`**: The central orchestrator.
    *   `generate_project(config)`: The main function that ties everything together.
    *   It initializes the `ProjectGenerator` to create files.
    *   It initializes `Integrations` to handle Git/Poetry/DVC.

*   **`generator.py`**: Handles file system operations.
    *   `ProjectGenerator`: Class responsible for creating directories and rendering templates.
    *   Uses `jinja2` to render files in `templates/` with the provided configuration.
    *   Auto-generates `README.md` files for subdirectories to document the generated project.

*   **`integrations.py`**: Wrappers for external tools.
    *   `Integrations`: Class that manages subprocess calls to `git`, `poetry`, and `dvc`.
    *   Handles error checking and provides user feedback via `rich`.

*   **`presets.py`**: Configuration management.
    *   `PresetsManager`: Handles loading and saving YAML configurations.
    *   Stores user presets in `~/.mlinit/presets/`.
    *   Includes default presets for General ML, CV, and NLP.

### Templates

The `templates/` directory contains Jinja2 templates (`.j2`) used to generate dynamic files like `train.py`, `README.md`, and CI/CD workflows.

## Adding New Features

*   **To add a new CLI command**: Edit `cli.py`.
*   **To change the project structure**: Edit the default structure in `presets.py` or the logic in `generator.py`.
*   **To add a new integration**: Add a method to `Integrations` in `integrations.py` and call it from `core.py`.
