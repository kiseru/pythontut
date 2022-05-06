import datetime

weekday = datetime.date.today().isoweekday()
print('Сегодня выходной!' if weekday in (6, 7) else 'Сегодня будний день, за работу!')
