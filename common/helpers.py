from re import sub


def replace_characters(string: str, regexp: str, replacement: str) -> str:
    return sub(regexp, replacement, string)
