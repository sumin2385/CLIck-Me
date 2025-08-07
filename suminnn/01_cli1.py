### 실습1 ###
# 가상환경 실행 명령어: hellopy-cli\Scripts\activate.bat
# 실행 명령어: python [본인_이름]/01_cli1.py

# ==========|코드 실습|========= #
import click

@click.command()

def main():
    print("Hello, HelloPY!")

if __name__ == "__main__":
    main()