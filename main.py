def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_words(text)
    characters = count_char(text)
    seznam = convert_dictionary(characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    
    for character, count in seznam:
        print(f"The '{character}' character was found {count} times")

    print("--- End report ---")

    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    number = len(words)
    return number

def count_char(text):
    text = text.lower()
    words = text.split()
    characters = {}
    for word in words:
        for character in word:
            if character.isalpha() == True:
                if character in characters:
                    characters[f"{character}"] += 1
                else:
                    characters[f"{character}"] = 1
    return characters    

def convert_dictionary(dictionary):
    key_value_list = list(dictionary.items())
    key_value_list.sort(reverse=True, key=lambda x: x[1])
    return key_value_list

    

main()