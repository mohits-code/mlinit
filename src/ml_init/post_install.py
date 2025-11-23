# src/ml_init/post_install.py
"""Post‑install hook for the mlinit‑cli package.

When the package is installed via ``pip`` this module is executed automatically.
It adds the Python ``Scripts`` directory (where the ``mlinit`` executable lives)
to the user's PATH if it is not already present, then prints a short reminder
to restart the terminal.
"""

import os
import sysconfig
import subprocess


def _add_to_path(scripts_dir: str) -> None:
    """Append ``scripts_dir`` to the user PATH if it isn’t already there.

    The function uses PowerShell to modify the *user‑level* environment variable
    because that is the most reliable way on Windows without requiring admin
    privileges.
    """
    # Retrieve the current user PATH
    current_path = os.environ.get("PATH", "")
    if scripts_dir.lower() in current_path.lower():
        return  # already present

    # Build a PowerShell command that appends the directory
    ps_cmd = [
        "powershell",
        "-Command",
        f"[Environment]::SetEnvironmentVariable('Path', $env:Path + ';{scripts_dir}', 'User')",
    ]
    # Run silently; we don’t need the output
    subprocess.run(ps_cmd, check=False)


def main() -> None:
    # Locate the Scripts directory for the interpreter that performed the install
    scripts_dir = sysconfig.get_path("scripts")
    if not os.path.isdir(scripts_dir):
        return
    _add_to_path(scripts_dir)
    print(
        f"\n[ml_init] Added '{scripts_dir}' to your user PATH. "
        "Please restart your terminal to use the `mlinit` command.\n"
    )


if __name__ == "__main__":
    main()
