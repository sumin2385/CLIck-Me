### 실습4 ###
# 실행 명령어1: python suminnn/01_cli4.py name
# 실행 명령어2: python [본인_이름]/01_cli4.py mbti

# ==========|코드 실습|========= #
import click

@click.group()
def main():
    pass

@main.command()
@click.option('--name', '-n', default='Pymon')
def name(name):
    click.echo(f"Hello, HelloPY!, My Name is {name}")

@main.command()
@click.option('--mbti', '-m', default='ENFJ')
def mbti(mbti):
    click.echo(f"Hello, HelloPY!, MBTI is {mbti}")

if __name__ == "__main__":
    main()
