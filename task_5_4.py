# Задача 5. Вариант 4.
# Напишите программу, которая бы при запуске случайным образом отображала
#один из трех цветов светофора.

# Badmaeva M.N.
# 12.10.2016

import random
colors = ("красный","зеленый","желтый")
vybor = random.choice(colors)
print("Программа случайным образом отображат цвет светофора")
print("Цвет светофора сейчас",vybor)
input("\nНажмите Enter для выхода")