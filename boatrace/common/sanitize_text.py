import re


def _delete_space_char(text: str) -> str:
    return text.replace("\u3000", "").replace(" ", "").replace("\t", "").replace("\xa0", "")


def _replace_line_break_duplicate_to_single(text: str) -> str:
    while "\n\n" in text:
        text = text.replace("\n\n", "\n")
    return text


def sanitize_text(text: str) -> str:
    """テキストから不要文字を削除"""
    text = _delete_space_char(text)
    text = _replace_line_break_duplicate_to_single(text)
    return text.strip()


def td_text_split(td_text: str) -> list[str]:
    """td要素内のテキストを改行ごとに分割"""
    text = sanitize_text(td_text)
    tokens = [token for token in re.split("[\n/]", text) if token.strip()]
    return tokens
