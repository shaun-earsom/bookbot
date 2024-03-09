def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_letters = count_letters(text)
    sort_letters = count_report(num_letters)
    print(f"--- Report of {book_path} ---")
    print(f"---- Word Count: {num_words}")
    print("---- Letter Breakdown:")
    for entry in sort_letters:
        print(f"---- {entry["char"]} appears {entry["count"]} times.")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            l_letter = letter.lower()
            if l_letter in letters:
                letters[l_letter] += 1
            else:
                letters[l_letter] = 1
    return letters

def sort_madness(dict):
    return dict["count"]

def count_report(l_dict):
    sort_list = []
    key_list = l_dict.copy().keys()
    for key in key_list:
        sort_list.append({"char": key, "count": l_dict[key]})
    sort_list.sort(reverse=True, key=sort_madness)
    return sort_list  

main()
