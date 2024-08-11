import string


BOOK_PATH = "./books/frankenstein.txt"


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_letters(text: str) -> dict:
    letters = {}
    ltext = text.lower()
    for c in string.ascii_lowercase:
        letters[c] = ltext.count(c)
    return letters


def sort_on_num(dicti: dict) -> int:
    return dicti["num"]


def sort_by_num(dicti: dict) -> list:
    listed = []
    for char in dicti.keys():
        listed.append({"char": char, "num": dicti[char]})
    listed.sort(reverse=True, key=sort_on_num)
    return listed


def openfile(book_path: str) -> str:
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    text = openfile(BOOK_PATH)
    print(f"--- Begin report of {BOOK_PATH} ---")
    print(f"The book has {count_words(text)} words")
    print()
    lettercount = count_letters(text)
    letterlist = sort_by_num(lettercount)
    for num in range(len(letterlist)):
        character = letterlist[num]
        print(
            f"The '{character["""char"""]}' character was found {character["""num"""]} times"
        )
    print("--- End report ---")


main()
