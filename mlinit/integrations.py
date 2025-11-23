import subprocess
import shutil
from rich.console import Console

console = Console()

class Integrations:
    def __init__(self, project_path):
        self.project_path = project_path

    def run_command(self, command, cwd=None, check=True):
        """Helper to run shell commands."""
        try:
            subprocess.run(
                command, 
                cwd=cwd or self.project_path, 
                check=check, 
                capture_output=True, 
                text=True
            )
            return True
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Command failed: {' '.join(command)}[/red]")
            console.print(f"[red]Error: {e.stderr}[/red]")
            return False
        except FileNotFoundError:
            console.print(f"[red]Command not found: {command[0]}[/red]")
            return False

    def init_git(self):
        """Initialize git repository."""
        console.print("Initializing Git repository...")
        if self.run_command(["git", "init"]):
            self.run_command(["git", "add", "."])
            self.run_command(["git", "commit", "-m", "Initial commit from mlinit"])
            console.print("[green]Git repository initialized.[/green]")

    def init_poetry(self, name, dependencies=None):
        """Initialize Poetry project."""
        console.print("Initializing Poetry...")
        if not shutil.which("poetry"):
            console.print("[yellow]Poetry not found. Skipping Poetry initialization.[/yellow]")
            return

        # Initialize poetry non-interactively
        if self.run_command(["poetry", "init", "--name", name, "--no-interaction"]):
            console.print("[green]Poetry initialized.[/green]")
            
            # Add dependencies
            deps = dependencies or ["hydra-core", "omegaconf"]
            console.print(f"Adding dependencies: {', '.join(deps)}...")
            for dep in deps:
                self.run_command(["poetry", "add", dep])
        else:
            console.print("[red]Failed to initialize Poetry.[/red]")

    def init_dvc(self):
        """Initialize DVC."""
        console.print("Initializing DVC...")
        if not shutil.which("dvc"):
             console.print("[yellow]DVC not found. Skipping DVC initialization.[/yellow]")
             return
        
        if self.run_command(["dvc", "init"]):
            console.print("[green]DVC initialized.[/green]")
