from datetime import date, datetime


today = date.today()
time = datetime.now().time().hour

new_year = date(day=31, month=12, year=date.today().year)

# Находим сколько дней осталось
day_rem = (new_year - today).days

# получаем оставшиеся часы
time = 24 - time

#  Настраиваем окончание
if (day_rem % 100) % 10 == 1 or day_rem % 10 > 4 or day_rem % 10 == 0:
    day_rem = (f'{day_rem} дней и {time}ч. осталось до Нового года')
elif day_rem % 10 == 1:
    day_rem = (f'{day_rem} день и {time}ч. осталось до Нового года')
else:
    day_rem = (f'{day_rem} дня и {time}ч. осталось до Нового года')

print(day_rem)
