import re
from typing import List


def get_list_of_words(text: str) -> List[str]:
    return re.findall(r"(\w+)", text, re.U)
