choice = None
while True:
    print("Вы решили прогуляться в Южном Бутово и наткнулись на спортивных ребят\n1. Попытаться убежать\n2. Продолжать идти")
    choice = int(input())

    if choice in range(1, 3):
        break

    print( "Выбран несуществующий вариант ответа. Попробуйте еще раз.")

if choice == 1:
    print( "Ребя без труда догнали вас и побили. Не знаю, за что")
else:
    while True:
        print("Один из ребят вышел вперёд и спросил \"Сиги есть?\"\n1. Дать прикурить\n2. -- Не курю")
        choice = int(input())
        if choice in range(1, 3):
            break

        print("Выбран несуществующий вариант ответа. Попробуйте еще раз.")

    if choice == 1:
        print("Прикурив, ребята отправились дальше")
    else:
        print("Ребята расстроились и побили вас. Теперь уже ясно, за что")