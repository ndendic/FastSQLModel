"""FastSQLModel CLI for initializing and managing Alembic migrations"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_cli.ipynb.

# %% auto 0
__all__ = ['app', 'process_templates', 'init', 'migrations']

# %% ../nbs/01_cli.ipynb 3
import typer
from rich import print
import subprocess
import os
import shutil
from pathlib import Path
from mako.template import Template

# %% ../nbs/01_cli.ipynb 5
app = typer.Typer(name="FastSQLModel CLI")

# %% ../nbs/01_cli.ipynb 7
def process_templates(template_dir: Path, target_dir: Path, script_location: str):
    """Process and copy template files with proper configuration"""
    # Create versions directory
    versions_dir = target_dir / 'versions'
    versions_dir.mkdir(exist_ok=True)
    
    # Copy static files to migrations directory
    for file_name in ['env.py', 'README', 'script.py.mako']:
        src = template_dir / file_name
        if src.exists():
            shutil.copy2(src, target_dir / file_name)
    
    # Process alembic.ini.mako and place it in the root directory
    template = Template(filename=str(template_dir / 'alembic.ini.mako'))
    config_content = template.render(script_location=script_location)
    
    
    # Write alembic.ini to the parent directory of migrations
    with open(target_dir.parent / 'alembic.ini', 'w') as f:
        f.write(config_content)

# %% ../nbs/01_cli.ipynb 9
@app.command(help="Initialize Alembic with custom FastSQLModel templates")
def init(
    directory: str = typer.Option(
        ".", 
        "--directory", "-d",
        help="Directory where to initialize Alembic (default: current directory)",
    )
):
    """
    Initialize a new Alembic environment with FastSQLModel templates.
    
    This will create:
    - alembic.ini in the root directory
    - migrations/ directory with:
        - env.py
        - README
        - script.py.mako
        - versions/ directory
    """
    try:
        # Get the template directory path relative to the cli.py file
        template_dir = Path(__file__).parent / 'templates'
        
        # Create migrations directory
        migrations_dir = Path(directory) / 'migrations'
        migrations_dir.mkdir(exist_ok=True)
        
        # Create versions directory
        versions_dir = migrations_dir / 'versions'
        versions_dir.mkdir(exist_ok=True)
        
        # Process and copy template files
        process_templates(
            template_dir=template_dir,
            target_dir=migrations_dir,
            script_location='migrations'
        )
        
        print("[green]Successfully initialized Alembic in migrations directory![/green]")
        print("[yellow]Please make sure to add your models to [underline]migrations/env.py[/underline] file before running migrations![/yellow]")
        
    except Exception as e:
        print(f"[red]Error initializing Alembic: {str(e)}[/red]")

# %% ../nbs/01_cli.ipynb 11
@app.command(help="Generate new Alembic migration")
def migrations(
    message: str = typer.Option(
        "Pushing changes",
        "--message", "-m",
        help="Migration message/description",
    ),
    autogenerate: bool = typer.Option(
        True,
        "--autogenerate/--no-autogenerate",
        help="Automatically generate migrations based on model changes",
    )
):
    """
    Generate a new Alembic migration file.
    
    Examples:
        fsm migrations -m "Add user table"
        fsm migrations --no-autogenerate -m "Custom migration"
    """
    print(f"Generating Alembic migration with message: {message}")
    try:
        cmd = ["alembic", "revision"]
        if autogenerate:
            cmd.append("--autogenerate")
        cmd.extend(["-m", message])
        subprocess.run(cmd, check=True)
        print("[green]Migration created successfully![/green]")
    except subprocess.CalledProcessError as e:
        print(f"[red]Error running Alembic: {e}[/red]")


# %% ../nbs/01_cli.ipynb 14
if __name__ == "__main__":
    app()
