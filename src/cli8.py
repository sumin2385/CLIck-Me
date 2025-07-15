### 실습8 ###
# 실행 명령어: python src/cli8.py

# ==========|코드 실습|========= #
import click
import pyfiglet
import time

from rich.table import Table
from rich.console import Console
from rich.progress import track
from rich.syntax import Syntax

@click.command()
def main():
    console = Console()

    code = """print(hellopy)"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    for step in track(range(10), description="Loading HelloPY..."):
        time.sleep(0.3)

    print(click.style(pyfiglet.figlet_format("HelloPY", font="doom"), fg="magenta"))
    click.echo(click.style(f"Hello, HelloPY World!", fg='magenta', bg='white', bold=True))
    click.echo("""
‘헬로파이 월드’는 파이썬을 배우고, 만들고, 함께 성장하는 주니어 개발자들의 세계를 상징합니다.
이곳의 ‘파이’는 단순한 디저트가 아닌, 문제를 해결하고 세상을 연결하려는 열정과 가능성을 담고 있죠.
🍋 레몬파이 마을에서는 처음 배우는 이들의 공부가,
🍎 애플파이 언덕에서는 프로젝트 아이디어가,
🍫 초코파이 숲에서는 협업과 성장의 기록이,
🫐 블루베리파이 호수에서는 깊이 있는 기여가 쌓여갑니다.
즉, 헬로파이 월드는 파이썬이라는 언어를 매개로
다양한 사람들이 함께 ‘굽고’, 나누고, 각자의 속도로 성장하는 커뮤니티의 세계관입니다.
하지만 지금, 헬로파이 월드에 이상 신호가 감지되고 있습니다.
과거의 인기 캐릭터 Pymon이 오븐의 불꽃을 꺼뜨리려 하며
시스템 곳곳에 오류가 발생하고, 파이들의 성장이 멈추고 있습니다.
🔥Pymon이 만든 에러를 해결하기 위해, 각 마을에서 파이크루(Pie Crew)가 모였습니다.
이제, 당신의 차례입니다.
불꽃을 되살리고, 헬로파이 월드를 지켜주세요.
""")

    table = Table(title=click.style("HelloPY 파이크루 소개"), style="purple")

    table.add_column("레벨", style="cyan")
    table.add_column("캐릭터명", justify="right")
    table.add_column("다음 단계 승급 조건 to-do", justify="right")
    table.add_column("승급 조건 만족 시, 보상", justify="right")

    table.add_row("LV0", "파이도우", "자기소개 채널에 자기소개 \n 온보딩 문서 정독 \n 가입 20분 이상 시 자동 승급", "✅ 모든 채널 접근 권한 \n ✅ 모든 활동 참여 가능")
    table.add_row("LV1", "레몬파이", "SNS 채널 팔로우 인증 \n 채팅 10회, 이모티콘 반응 30회 이상 \n 프로젝트 참여 3회 이상 \n 발표 1회 이상", "활동 참여 자격 획득")
    table.add_row("LV2", "애플파이", "활동 참여 1회 이상 \n 채팅 50회, 이모지 반응 100회, 가입 30일 이상", "굿즈 응모권 제공")
    table.add_row("LV3", "초코파이", "리딩 경험 보유 \n 채팅 100회, 이모지 반응 200회, 가입 30일 이상", "멘토 미팅 커리어 코칭")
    table.add_row("LV4", "블루베리파이", "(운영진 지정 또는 신청 기준)", "HelloPY 티셔츠 \n 제안자 권한 전용 배지")

    console.print(table)

if __name__ == "__main__":
    main()

