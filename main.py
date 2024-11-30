def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(book_path)
    char_count = character_count(text)
    sorted_char_count = sorted_char_list(char_count)

    print(f"---- Begin report of {book_path} ----")
    print(f"{word_count} words found in the document")
    print("")
    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"The '{char["char"]}' character was found {char["num"]} times")
    print("")
    print("---- End of report ----")
        


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(path):
    text = get_book_text(path)
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sorted_char_list(char_count):
    sorted_list = []
    for key in char_count:
        sorted_list.append({"char": key, "num": char_count[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

main()
