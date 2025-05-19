import re

def extract_data(text):
    results = {
        "emails": re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text),
        "urls": re.findall(r"https?://[^\s]+", text),
        "phones": re.findall(r"\(?\+?250\)?[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{3}|\(?250\)?[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{3}|\(?0\d{2}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text),
        "credit_cards": [cc for cc in re.findall(r"(?:\d{4}[-\s]?){4}", text) if len(cc.replace('-', '').replace(' ', '')) == 16],
        "hashtags": re.findall(r"#\w+", text),
        "times": re.findall(r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b", text)
    }
    return results

if __name__ == "__main__":
    with open("test_cases.txt", "r") as file:
        content = file.read()
        extracted = extract_data(content)
        for key, values in extracted.items():
            print(f"\n{key.upper()}:")
            for value in values:
                print(" -", value)
