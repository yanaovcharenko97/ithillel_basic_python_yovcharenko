text = input('Введіть будь який текст:\n')

print(f'\nТретій символ тексту: {text[2]}\n'
      f'Передостанній символ тексту: {text[-2]}\n'
      f'Перші пять символів тексту: {text[:5]}\n'
      f'Весь текст, окрім 2 останніх символів: {text[:-2]}\n'
      f'Усі символи тексту з парними індексами: {text[::2]}\n'
      f'Усі символи тксту з непарними індексами: {text[1::2]}\n'
      f'Весь текст у зворотньому напрямку: {text[::-1]}\n'
      f'Текст у зворотньому, через один символ: {text[::-2]}\n'
      f'Довжина тексту: {len(text)} символів')