chosen_currency = int(input("Какая у вас на руках валюта?\n1. Рубли\n2. Доллары\n"))
dollar_cost = float(input("Сколько сейчас стоит 1 доллар?\n"))
if chosen_currency == 1:
    print("Сколько у вас рублей?")
else:
    print("Сколько у вас долларов?")

currency_amount = float(input())
if chosen_currency == 1:
    converted_currency_amount = currency_amount / dollar_cost
    print(f"Ваши запасы на сегодня равны: {converted_currency_amount} $")
else:
    converted_currency_amount = currency_amount * dollar_cost
    print(f"Ваши запасы на сегодня равны: {converted_currency_amount} руб.")
