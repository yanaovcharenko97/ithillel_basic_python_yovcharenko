from math import *
number = input("Введіть будь яке число (радіани), щоб розрахувати його тангенс: ")
number = int(number)
print(sqrt(1-cos(number)**2) / cos(number))
