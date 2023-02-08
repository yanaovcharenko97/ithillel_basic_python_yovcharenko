text = input('Please enter text (in format world_world_world): ')
text = text.split('_')

print('\nResult:', text[0].capitalize() + text[1].capitalize() + text[2].capitalize())
