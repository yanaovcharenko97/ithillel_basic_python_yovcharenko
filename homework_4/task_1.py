text = input('Please enter text (in format world_world_world): ')

print('\nResult:', text.split('_')[0].capitalize() + text.split('_')[1].capitalize() + text.split('_')[2].capitalize())
