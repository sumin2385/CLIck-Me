### 실습6 ###
# 실행 명령어: python suminnn/01_cli6.py

# ==========|코드 실습|========= #
import click
import pyfiglet

@click.command()
def main():
    click.echo(pyfiglet.figlet_format("WoW AmaZing", font="bulbhead"))

if __name__ == "__main__":
    main()