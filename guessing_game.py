import random

NUMBER_OF_ATTEMPTS = 3
INTERVAL_START = 0
INTERVAL_END = 16

is_won = False


def generate_number_to_guess(interval_start, interval_end):
    number_to_guess = random.randrange(interval_start, interval_end)
    print(f"Загадано число от {interval_start} до {interval_end}, отгадайте какое?")
    return number_to_guess


def make_attempt(attempt, number_to_guess):
    check_attempt(attempt, number_to_guess)
    give_hint(attempt, number_to_guess)


def check_attempt(attempt, number_to_guess):
    if attempt == number_to_guess:
        print("Ура, вы выиграли!")
        global is_won
        is_won = True


def give_hint(attempt, number_to_guess):
    if not is_won:
        say_need_more_or_less(attempt, number_to_guess)
        say_hot_or_cold(attempt, number_to_guess)


def say_need_more_or_less(attempt, number_to_guess):
    if attempt > number_to_guess:
        print("нужно меньше")
    else:
        print("нужно больше")


def say_hot_or_cold(attempt, number_to_guess):
    if abs(attempt - number_to_guess) < 3:
        print("Тепло")
    else:
        print("Холодно")


number_to_guess = generate_number_to_guess(INTERVAL_START, INTERVAL_END)
for _ in range(NUMBER_OF_ATTEMPTS):
    attempt = int(input())
    make_attempt(attempt, number_to_guess)
    if is_won:
        break

if not is_won:
    print(f"В этот раз вам не повезло. Было загадано число {number_to_guess}")
