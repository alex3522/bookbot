def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letterset = create_letter_set(text)
    letter_dict = count_letters(text, letterset)
    letter_sorted_list = dict_to_listdict(letter_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in letter_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

### get number of words in the text
def get_num_words(text):
    words = text.split()
    return len(words)

### reads book based on path and converts to lower case
def get_book_text(path):
    with open(path) as f:
        return f.read().lower()
    
### create a set of all characters then sort alphabetically
def create_letter_set(text):
    letters = sorted(set(text))
    return letters

### create dictionary of letters and counts, only if they're letters
def count_letters(text, letters):
    letter_dict = {}
    for letter in letters:
        if letter.isalpha():
            letter_dict[letter] = text.count(letter)
    return letter_dict

### sorting function
def sort_on(d):
    return d["num"]


### create sorted list of dictionaries
def dict_to_listdict(letter_dict):
    sorted_list = []
    for letter in letter_dict:
        sorted_list.append({"char": letter, "num": letter_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()