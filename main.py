def __main__():
    print_report("books/frankenstein.txt")


def get_character_dict(text: str) -> dict:
    char_list = list(text)
    char_dict = {}

    for char in char_list:
        lowercase_char = char.lower()
        if (lowercase_char in char_dict):
            char_dict[lowercase_char] += 1
        else:
            char_dict[lowercase_char] = 1

    return char_dict


def print_report(path: str):
    with open(path) as f:
        file_contents = f.read()
        char_dict = get_character_dict(file_contents)

        sorted_char_dict = sorted(char_dict, reverse=True, key=char_dict.get)

        print(f"--- Begin report of {path} ---")
        print(f"{count_words(file_contents)} words found in the text.\n")
        for char in sorted_char_dict:
            if char.isalpha():
                print(f"The '{char}' character was found {
                      char_dict[char]} times.")
        print(f"\n--- End report of {path} ---")


def count_words(text: str) -> int:
    return len(text.split())


if __name__ == "__main__":
    __main__()
