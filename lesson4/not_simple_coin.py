import random

a = random.random()
if a < 0.1:
    print("Монета встала на ребро")
elif a < 0.55:
    print("Выпал орел")
else:
    print("Выпала решка")
