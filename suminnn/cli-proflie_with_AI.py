import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import click
import pyfiglet
from rich.box import ROUNDED
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.rule import Rule
from rich.table import Table

# CLI 출력을 위한 Rich 콘솔 인스턴스
console = Console()


def load_developer_data(data_file: Path) -> Dict[str, Any]:
    """JSON 파일에서 개발자 정보를 로드합니다."""
    try:
        with data_file.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"[red]오류: {data_file} 파일을 찾을 수 없습니다.[/red]")
        sys.exit(1)
    except json.JSONDecodeError as e:
        console.print(f"[red]오류: JSON 파싱 실패 - {e}[/red]")
        sys.exit(1)


def print_initial(initials: str, name: str) -> None:
    """개발자 이름과 이니셜을 ASCII 아트로 출력합니다."""
    figlet_text = pyfiglet.figlet_format(initials, font="slant")
    console.print(
        Panel(
            f"[bold cyan]{figlet_text}[/bold cyan]",
            title=f"[white bold]{name}님의 프로필[/white bold]",
            border_style="bright_blue",
            padding=(1, 2),
            expand=False,
            subtitle="[cyan]Welcome to my CLI Profile![/cyan]",
        )
    )
    console.print()


def print_intro(intro: str) -> None:
    """자기소개 문구를 출력합니다."""
    console.print(f'[italic yellow]"{intro}"[/italic yellow]', justify="center")
    console.print()


def print_skills_table(skills: Dict[str, List[str]]) -> None:
    """기술 스택을 Rich Table 형태로 출력합니다."""
    if not skills:
        return
    table = Table(
        title="[bold]🛠️ 기술 스택[/bold]",
        box=ROUNDED,
        border_style="cyan",
        header_style="bold cyan",
        title_justify="left",
    )
    table.add_column("분야", style="green", no_wrap=True)
    table.add_column("기술", style="magenta")

    for category, skill_list in skills.items():
        table.add_row(category, ", ".join(skill_list))

    console.print(table)
    console.print()


def print_activities_table(activities: List[Dict[str, str]]) -> None:
    """동아리 활동 정보를 Rich Table 형태로 출력합니다."""
    if not activities:
        return

    table = Table(
        title="[bold]🚀 동아리 활동[/bold]",
        box=ROUNDED,
        border_style="green",
        header_style="bold green",
        title_justify="left",
    )
    table.add_column("활동명", style="cyan")
    table.add_column("역할", style="green")
    table.add_column("설명", style="magenta")

    for activity in activities:
        table.add_row(
            activity.get("name", ""),
            activity.get("role", ""),
            activity.get("description", ""),
        )
    console.print(table)
    console.print()


def print_education_info(education: Dict[str, str]) -> None:
    """학력 정보를 Rich Table 형태로 출력합니다."""
    if not education:
        return

    table = Table(
        title="[bold]🎓 학력[/bold]",
        box=ROUNDED,
        border_style="yellow",
        header_style="bold yellow",
        title_justify="left",
    )
    table.add_column("항목", style="cyan", no_wrap=True)
    table.add_column("내용", style="magenta")

    education_labels = {
        "university": "대학교",
        "major": "전공",
        "expected_graduation": "졸업 예정",
    }

    for key, label in education_labels.items():
        if key in education:
            table.add_row(label, education[key])

    console.print(table)
    console.print()


def print_contact_info(contact: Dict[str, str]) -> None:
    """연락처 정보를 Rich Table 형태로 출력합니다."""
    if not contact:
        return

    table = Table(
        title="[bold]📞 연락처[/bold]",
        box=ROUNDED,
        border_style="magenta",
        header_style="bold magenta",
        title_justify="left",
    )
    table.add_column("채널", style="cyan", no_wrap=True)
    table.add_column("링크", style="magenta")

    for channel, link in contact.items():
        # Make links clickable in supported terminals
        if "http" in link or "mailto" in link:
            table.add_row(channel.capitalize(), f"[link={link}]{link}[/link]")
        else:
            table.add_row(channel.capitalize(), link)

    console.print(table)
    console.print()


@click.command()
@click.option(
    "--data-path",
    type=click.Path(exists=True, path_type=Path),
    help="data.json 파일 경로(기본값: data.json)",
)
@click.option("--no-skills", is_flag=True, help="기술 스택 정보를 숨깁니다.")
@click.option("--no-activities", is_flag=True, help="동아리 활동 정보를 숨깁니다.")
@click.option("--no-education", is_flag=True, help="학력 정보를 숨깁니다.")
@click.option("--no-contact", is_flag=True, help="연락처 정보를 숨깁니다.")
def main(
    data_path: Optional[Path] = None,
    no_skills: bool = False,
    no_activities: bool = False,
    no_education: bool = False,
    no_contact: bool = False,
) -> None:
    """CLI에서 개발자 프로필을 출력합니다."""
    for _ in track(range(10), description="Processing..."):
        time.sleep(0.1)  # 로딩 애니메이션 효과를 위해 잠시 대기

    # 기본 경로 설정
    if data_path is None:
        data_path = Path(__file__).parent / "data.json"

    developer_data = load_developer_data(data_path)

    # JSON에서 데이터 추출 (기본값 처리 포함)
    initials = developer_data.get("initials")
    name = developer_data.get("name", "Unknown")
    # 'initials' 키가 없으면 'name'으로 생성
    if not initials:
        initials = "".join([part[0].upper() for part in name.split()])

    intro = developer_data.get("intro", "")
    skills = developer_data.get("skills", {})
    activities = developer_data.get("activities", [])
    education = developer_data.get("education", {})
    contact = developer_data.get("contact", {})

    print_initial(initials, name)
    print_intro(intro)

    console.print(Rule(style="bright_black"))

    # 플래그 옵션에 따라 정보 출력 여부 결정
    if not no_education:
        print_education_info(education)
    if not no_skills:
        print_skills_table(skills)
    if not no_activities:
        print_activities_table(activities)
    if not no_contact:
        print_contact_info(contact)

    console.print(Rule(style="bright_blue"))
    console.print("[bold green]봐주셔서 감사합니다! 😄[/bold green]", justify="center")


if __name__ == "__main__":
    main()
#