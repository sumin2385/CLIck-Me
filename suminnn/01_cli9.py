### 실습9 ###
# 실행 명령어: python [본인_이름]/01_cli9.py

# ==========|코드 실습|========= #
from rich.console import Console
from rich.progress import track
import time

for step in track(range(10), description="Processing..."):
    time.sleep(0.5)