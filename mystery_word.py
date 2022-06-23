import random


def play_game():
    read_file = read_text_file()
    random_word = get_random_word(read_file)
    print(f"Answer: {random_word}")

    start_of_game(random_word)
    user_guess(random_word)


def read_text_file():
    text_file = "words.txt"
    with open(text_file) as open_file:
        read_file = open_file.read()

    word_list = read_file.split()

    return word_list


def get_random_word(words):
    words_length = len(words)
    random_number = random.randrange(0, words_length)
    random_word = words[random_number]
    upper_case_random_word = random_word.upper()

    return upper_case_random_word


def start_of_game(word):
    word_length = len(word)
    underscore_value = "_" * word_length

    print("Hello! Let's play a word guessing game!")
    print(f"The mystery word has {word_length} characters: {underscore_value}")
    print("You will have 8 guesses!")
    print()


def check_user_input():
    pass


def user_guess(word):
    pass


if __name__ == "__main__":
    play_game()
