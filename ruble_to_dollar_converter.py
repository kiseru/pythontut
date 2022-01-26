dollar_cost = float(input("Сколько сейчас стоит 1 доллар в рублях? "))
rubles_amount = float(input("Сколько сейчас у вас рублей? "))
dollars_amount = round(rubles_amount / dollar_cost, 2)
print(f"Ваши запасы равны: ${dollars_amount}")
