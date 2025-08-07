### 실습2 ###
# 실행 명령어: python [본인_이름]/01_cli2.py
# 실행 명령어: python suminnn/01_cli2.py --name CLIck-Me

# ==========|코드 실습|========= #
import click

@click.command()
@click.option('--name', '-n', default='Pymon')

def main(name):
    print("Hello, HelloPY!, My Name is", name)

if __name__ == "__main__":
    main()