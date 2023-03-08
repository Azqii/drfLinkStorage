import re


def is_url(value: str) -> bool:
    """Checks if the value is an url"""
    pattern = re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
    return True if re.search(pattern, value) else False
