### 실습5 ###
# 실행 명령어: python suminnn/01_cli5.py

# ==========|코드 실습|========= #
import click

@click.command()
@click.option('--name', '-n', default='Pymon')
def main(name):
    click.echo(click.style(f"Hello, HelloPY!, My Name is {name}", fg='red', bg='cyan', bold=True))

if __name__ == "__main__":
    main()
