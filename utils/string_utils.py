import re


def extract_chinese(text):
    """只匹配文本前面的中文"""

    if text and (text[0].isalpha() or text[0] == "（" or text[0].isdigit()):
        return text
    else:
        pattern = r'^[\u4e00-\u9fff]+'
        match = re.search(pattern, text)
        if match:
            chinese_text = match.group()
            return chinese_text
        else:
            return ''
