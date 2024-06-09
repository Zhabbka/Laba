import re

def punctuation_ru(data: str) -> str:
    return re.sub(r'[^\w\s]', '', data).strip()

if __name__ == "__main__":
    data = input().strip()
    print(punctuation_ru(data))
