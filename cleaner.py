import re
 
def clean_text(text: str) -> str:

    if not isinstance(text, str):
        raise ValueError("input value must be string")

    text = re.sub(r"\\s+", " ", text)

    text = re.sub(r"[^a-zA-Z0-9.,!? ]+", "", text)

    text = text.strip()

    return text

def fix_pdf_lines(text: str) -> str:
    text = text.replace("/n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


