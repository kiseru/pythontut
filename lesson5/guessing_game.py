import random

NUMBER_OF_ATTEMPTS = 3
INTERVAL_START = 0
INTERVAL_END = 16

number_to_guess = random.randrange(INTERVAL_START, INTERVAL_END)
is_won = False
for _ in range(NUMBER_OF_ATTEMPTS):
    attempt = int(input(f"Загадано число от {INTERVAL_START} до {INTERVAL_END}, отгадайте какое? "))

    if attempt == number_to_guess:
        print("Ура, вы выиграли!")
        is_won = True
        break

    if attempt > number_to_guess:
        print("нужно меньше")
    else:
        print("нужно больше")

    if abs(attempt - number_to_guess) < 3:
        print("Тепло")
    else:
        print("Холодно")

if not is_won:
    print(f"В этот раз вам не повезло. Было загадано число {number_to_guess}")
