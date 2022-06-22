import random
# from nbformat import read


def play_game():
    read_file = read_text_file()
    random_word = get_random_word(read_file)
    start_of_game(random_word)


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

    return random_word


def start_of_game(word):
    word_length = len(word)
    print(f"The word has {word_length} characters.")
    print("_" * word_length)
    print(f"Answer = {word}")


if __name__ == "__main__":
    play_game()
