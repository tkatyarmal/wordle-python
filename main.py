import random
from art import logo
from words_list import words

print(logo)

attempts_remaining = 5
word_to_guess = random.choice(words)
game_started = True
hints_enabled = False


def calculate(user_guess, answer):
    user_guess = user_guess.lower()
    answer = answer.lower()
    return_list = []

    if user_guess == answer:
        return "Word found"

    for i in range(len(user_guess)):
        if user_guess[i] == answer[i]:
            return_list.append("🟩")
        elif user_guess[i] in answer:
            return_list.append("🟧")
        else:
            return_list.append("🟥")
    return return_list


def show_hint():
    if hints_enabled:
        print(f"Word to guess: {word_to_guess}")


while game_started:
    print(f"You have {attempts_remaining} attempts remaining")
    show_hint()

    guess = input(f"What is your guess?: ")
    result = calculate(guess, word_to_guess)

    if result == "Word found":
        print("You have guessed the word correctly")
        print("You win")
        game_started = False
    else:
        print(result)
        attempts_remaining -= 1

    if attempts_remaining == 0:
        print(f"You could not guess the word. The word was {word_to_guess}")
        print("You lose")
        game_started = False

