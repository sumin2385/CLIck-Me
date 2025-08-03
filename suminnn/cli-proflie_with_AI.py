### Homework ###
# 실행 명령어: python [본인_이름]/cli-proflie_with_AI.py

# ==========|코드 실습|========= #
#!/usr/bin/env python3
"""
cli-proflie.py
--------------

CLI를 통해 개발자를 소개하는 스크립트.
사용자는 data.json에 정보를 입력한 뒤, 이 스크립트를 실행하면
이니셜, 자기소개, 기술 스택 표를 보여준다.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

import click 
import pyfiglet
from rich.box import ROUNDED
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table

# CLI 출력을 위한 Rich 콘솔 인스턴스
console = Console()


def load_developer_data(data_file: Path) -> Dict[str, Any]:
    """
    data.json 파일에서 개발자 정보를 로드한다.

    Parameters
    ----------
    data_file : Path
        개발자 정보가 담긴 JSON 파일 경로

    Returns
    -------
    Dict[str, Any]
        개발자 정보 JSON 객체

    Raises
    ------
    FileNotFoundError
        data.json이 존재하지 않을 경우
    json.JSONDecodeError
        JSON 파싱 오류 발생 시
    """
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
    """
    개발자 이니셜을 Figlet 폰트로 Panel에 담아 출력한다.

    Parameters
    ----------
    initials : str
        개발자 이니셜
    name : str
        개발자 이름
    """
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
    """
    한 줄 자기소개를 출력한다.

    Parameters
    ----------
    intro : str
        자기소개 문구
    """
    console.print(f'[italic yellow]"{intro}"[/italic yellow]', justify="center")
    console.print()


def print_skills_table(skills: Dict[str, List[str]]) -> None:
    """
    기술 스택을 표 형태로 출력한다.

    Parameters
    ----------
    skills : Dict[str, List[str]]
        기술 스택 딕셔너리
        {"분야": ["기술1", "기술2"], ...} 형태
    """
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
    """
    대외활동 정보를 표 형태로 출력한다.

    Parameters
    ----------
    activities : List[Dict[str, str]]
        대외활동 리스트
        각 항목은 {"name": ..., "role": ..., "description": ...} 형태
    """
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
    """
    학력 정보를 표 형태로 출력한다.

    Parameters
    ----------
    education : Dict[str, str]
        {"university": ..., "major": ..., "expected_graduation": ...} 형태의 학력 딕셔너리
    """
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
    """
    연락처 정보를 표 형태로 출력한다.

    Parameters
    ----------
    contact : Dict[str, str]
        {"email": ..., "github": ..., "linkedin": ...} 형태의 연락처 딕셔너리
    """
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
def main(data_path: Path | None = None) -> None:
    """
    CLI에서 개발자를 소개하는 메인 함수.
    """
    # 기본 경로 설정
    if data_path is None:
        data_path = Path(__file__).with_name("data.json")

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

    print_skills_table(skills)
    print_activities_table(activities)
    print_education_info(education)
    print_contact_info(contact)

    console.print(Rule(style="bright_blue"))
    console.print("[bold green]봐주셔서 감사합니다! 😄[/bold green]", justify="center")


if __name__ == "__main__":
    main()

#아니 왜안됨