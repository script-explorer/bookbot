# print("hello world")
def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)

    char_dict = count_chars(file_contents)
    return word_count, char_dict

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_chars(file_contents):
    # words = file_contents.split()

    char_dict = {}

    for char in file_contents.lower():
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] = 1
    
    return char_dict


if __name__ == "__main__":
    word_count, char_dict = main()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print(char_dict)

    keys = list(char_dict.keys())
    values = list(char_dict.values())

    for key, value in zip(keys, values):
        print(f"The character '{key}' was found {value} times.")

