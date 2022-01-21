import datetime

weekday = datetime.date.today().isoweekday()
if weekday == 6 or weekday == 7:
    print("Сегодня выходной!")
else:
    print("Сегодня будний день, за работу!")
