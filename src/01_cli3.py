### 실습3 ###
# 실행 명령어1: python src/01_cli3.py --name CLIck-Me
# 실행 명령어2: python src/01_cli3.py --mbti ENFJ

# ==========|코드 실습|========= #
import click

@click.command()
@click.argument()
def main():
    pass


if __name__ == "__main__":
    main()