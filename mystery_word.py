import random


def play_game():
    read_file = read_text_file()
    random_word = get_random_word(read_file)
    # print(f"Answer: {random_word}")

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
    while True:
        user_value = input("Please enter a single character value: ")
        user_length = len(user_value)

        if user_length == 1:
            if user_value.isalpha():
                return user_value.upper()
                # print(user_value)
                # break
            else:
                print("Invalid input! Only enter a character value!")  
        else:
            print("Invalid input! Only enter a single value!")

    # return user_value


#can break down into several steps
def user_guess(word):
    guess_list = []
    count = 8
    # length_list = len(guess_list)

    while count > 0:
        user_input = check_user_input()

        if user_input in guess_list:
            print("You have already guessed this character!")
        else:
            guess_list.append(user_input)
            count -= 1
            # print(f"You have {count} guesses left!")

            if user_input in word:
                blank_canvas = [i if i in guess_list else (i.replace(i, "_")) for i in word]
                # print(blank_canvas)

                print("".join(blank_canvas))

                if "_" not in blank_canvas:
                    print("Congrats, you guessed the word!")
                    break

                if count != 0:
                    print(f"You have {count} guesses left!")
                else:
                    print("Sorry, you lost the game!")
                    print(f"The mystery word was: {word}")
            else:
                if count != 0:
                    print("Try again! Letters guessed:", guess_list)
                    print(f"You have {count} guesses left!")
                else:
                    print("Sorry, you lost the game!")
                    print(f"The mystery word was: {word}")


if __name__ == "__main__":
    play_game()
