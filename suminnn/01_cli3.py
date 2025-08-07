### 실습3 ###
# 실행 명령어1: python [본인_이름]/01_cli3.py --name CLIck-Me
# 실행 명령어2: python suminnn/01_cli3.py --mbti ENFJ

# ==========|코드 실습|========= #
import click

@click.command()
@click.option('--name', '-n', default='Pymon')
@click.option('--mbti', '-m', default='MBTI')

def main(name, mbti):
    print(f"Hello, HelloPY!, My Name is {name}, MBTI is {mbti}")

if __name__ == "__main__":
    main()