from datetime import datetime
from pathlib import Path
import re

START_YEAR = 2022
README_PATH = Path("README.md")

current_year = datetime.now().year
years = current_year - START_YEAR

experience_text = f"{years}+"

content = README_PATH.read_text(encoding="utf-8")

new_content = re.sub(
    r"<!--EXPERIENCE-->.*?<!--/EXPERIENCE-->",
    f"<!--EXPERIENCE-->{experience_text}<!--/EXPERIENCE-->",
    content,
    flags=re.DOTALL,
)

README_PATH.write_text(new_content, encoding="utf-8")