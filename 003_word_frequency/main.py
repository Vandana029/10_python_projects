from collections import Counter
import re

def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    # r'\b\w+\b': find all the words in the sentences 
    # which are alphanumeric and which contain underscores.
    words: list[str] = re.findall(r'\b\w+\b')
    word_counts: Counter = Counter(words)
    return 


def main() -> None:
    # .strip(): strip the leading whitespaces and the trailing white spaces.
    text: str = input('Enter the text: ').strip()
    word_frequencies: list[tuple[str, int]] = get_frequency(text)
    print(word_frequencies)


if __name__ == '__main__':
    main()
