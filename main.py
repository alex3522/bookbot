def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path).lower()
    num_words = get_num_words(text)
    letterset = sorted(create_letter_set(text))
    letter_dict = count_letters(text, letterset)
    print(f"{num_words} words found in the document")
    print(letter_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def create_letter_set(text):
    letters = set(text)
    return letters


def count_letters(text, letters):
    letter_dict = {}
    for letter in letters:
        if letter.isalpha():
            letter_dict[letter] = text.count(letter)
    return letter_dict
        

main()