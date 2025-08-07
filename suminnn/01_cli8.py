### 실습8 ###
# 실행 명령어: python [본인_이름]/01_cli8.py

# ==========|코드 실습|========= #
import click
from rich.console import Console
from rich.markdown import Markdown

import click
from rich.console import Console
from rich.markdown import Markdown
console = Console()

@click.command()
def main():
    md = Markdown("""# **👾 퀘스트 개요**
- `click`, `rich`, `pyfiglet` 라이브러리를 활용하여, 간단한 **Python CLI 프로그램**을 제작합니다.
```py
# HelloPY!
print("Hello, HelloPY!")
```
""")
    console.print(md)
if __name__ == "__main__":
    main()