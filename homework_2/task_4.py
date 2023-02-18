from decimal import *
number = Decimal(input('Введіть кількість гривенень: '))
exchange = Decimal('37.44')
result = number / exchange
print(f"Станом на 30 січня 2023 року це становить", round(result, 2), "доларів США")
