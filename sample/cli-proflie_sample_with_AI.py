### Week2 sample ###
# 실행 명령어: python sample/cli-proflie_sample_with_AI.py

# ==========|코드 실습|========= #
import click
import pyfiglet
import time

from rich.console import Console
from rich.progress import track
from rich.syntax import Syntax
from rich.table import Table

@click.command()
def main():
    console = Console()

    # ASCII Art Welcome
    console.print(click.style(pyfiglet.figlet_format("Hello, I'm Your AI Assistant!", font="slant"), fg="green"))
    click.echo(click.style("Welcome to my CLI profile!", fg='cyan', bold=True))
    click.echo("\n")

    # Loading animation
    for step in track(range(20), description="Loading profile data..."):
        time.sleep(0.1)

    # Introduction
    console.print(click.style("About Me:", fg="magenta", bold=True))
    console.print("I am an AI programming assistant designed to help you with code generation and understanding.")
    console.print("I specialize in Python, but I can assist with various other programming languages as well.")
    console.print("\n")

    # Skills Table
    table = Table(title="[gold3]My Core Skills[/gold3]")
    table.add_column("Category", style="cyan")
    table.add_column("Skills", justify="left", style="white")

    table.add_row("Programming Languages", "Python, JavaScript, Go, Ruby, etc.")
    table.add_row("Frameworks/Libraries", "Click, Rich, Pyfiglet, Django, Flask, React, TensorFlow, PyTorch")
    table.add_row("Tools", "Git, Docker, Kubernetes, VS Code")
    table.add_row("Concepts", "CLI Development, Web Development, Machine Learning, Data Science")
    console.print(table)
    console.print("\n")

    # Code Example
    console.print(click.style("Here's a snippet of how I might generate Python code:", fg="magenta", bold=True))
    code_example = """
import click

@click.command()
@click.option('--name', default='World', help='The name to greet.')
def greet(name):
    click.echo(f'Hello, {name}!')
"""
    syntax = Syntax(code_example, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
    console.print("\n")

if __name__ == "__main__":
    main()