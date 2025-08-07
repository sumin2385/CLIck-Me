### 실습10 ###
# 실행 명령어: python suminnn/01_cli10.py

# ==========|코드 실습|========= #
from rich.syntax import Syntax
from rich.console import Console

console = Console()
code = "def hello():\n    print('Hello, HelloPY world!')"
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)

console.print(syntax)