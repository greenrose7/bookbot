def main():
    target_book = "books/frankenstein.txt"
    with open(target_book) as f:
        file_contents = f.read()
        print(file_contents)

        print(f"--- Begin report of {target_book} ---")

        print(f"There are {count_words(file_contents)} words in this text!")
        print("")
        print("Character breakdowns:")
        character_counts = count_characters(file_contents)
        sorted_character_counts = sorted(character_counts.items(), reverse = True, key=lambda x:x[1])
        # print(sorted_character_counts)

        for i in sorted_character_counts:
            if i[0].isalpha():
                print(f"The '{i[0]}' character was found {i[1]} times")


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_counts = {}
    for c in text:
        if not c in character_counts:
            character_counts[c] = 0
        character_counts[c] += 1
    
    return character_counts


main()