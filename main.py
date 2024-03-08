def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_letters = count_letters(text)
    print(f"{num_words} words found in the document")
    print(f"Letter Report: {num_letters}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        l_letter = letter.lower()
        if l_letter in letters:
            letters[l_letter] += 1
        else:
            letters[l_letter] = 1
    return letters

main()
