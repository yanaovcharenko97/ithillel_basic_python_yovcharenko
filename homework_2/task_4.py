from decimal import *
number = Decimal(input('Введіть кількість гривенень: '))
exchange = Decimal('37.44')
print(f"Станом на 30 січня 2023 року це становить {number * exchange} доларів США")
