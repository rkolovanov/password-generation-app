import string
import random
from re import sub


def replace_characters(string: str, regexp: str, replacement: str) -> str:
    return sub(regexp, replacement, string)


def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits
    return "".join([random.choice(characters) for _ in range(length)])
