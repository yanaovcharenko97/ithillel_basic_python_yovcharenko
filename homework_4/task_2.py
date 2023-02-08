text = input('Please enter name, date of berth, date of death (in the format Name*yyyy-mm-dd*yyyy-mm-dd):\n')
text = text.split('*')

a = "".join(text[1]).split('-')
b = "".join(text[2]).split('-')

print(f'\nName: {text[0]}\nAge: {int(b[0])-int(a[0])} years')
