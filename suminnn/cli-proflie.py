import click
import time
import pyfiglet
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import track
from rich.syntax import Syntax

@click.command()
def main():
    console = Console()
    click.echo("\n")
    click.echo(pyfiglet.figlet_format("     Profile", font="roman"))
    for step in track(range(10), description="Processing..."):
        time.sleep(0.2)
    
    code = "import 서수민\n\ndef 소개하기():\n    print(\"안녕하세요, 서수민입니다\") \n    Age = 21\n    Major = '정보통신공학과'\n    MBTI = 'ISFP'\n\ndef 취미():\n"
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
   
    table = Table(title=click.style("    저는 취미가 많습니다", fg = 'bright_green', bold = True), style="bright_green")

    table.add_column("관심사", style="green")
    table.add_column(" ")

    table.add_row("악기🎹", "찍먹 좋아해서 피아노, 플룻, 기타, 첼로, 색소폰 배워봤어요\n")
    table.add_row("그림🎨", "초등학교 과학상상화를 휩쓸었습니다😎\n")
    table.add_row("축구관람⚽", "포항스틸러스 우승기원 !!\n")
    table.add_row("게임🎮", "하는 것도 보는 것도 좋아해요\n")
    table.add_row("밴드🎵", "밴드음악 좋아하고, 밴드부도 하고있어요")
    console.print(table)

    md1 = Markdown("`멋진 분들`과 함께하게 되어 **영광입니다**.")
    md2 = Markdown("많이 부족하지만 `열심히 하겠습니다!`")
    md3 = Markdown("# **😄 감사합니다!😄**")
    click.echo("\n")
    console.print(md1)
    console.print(md2)
    console.print(md3)


if __name__ == "__main__":
    main()
#