# Задача 4. Вариант 4.
# Напишите программу, которая выводит имя, под которым скрывается Джон
#Гриффит Лондон. Дополнительно необходимо вывести область интересов
#указанной личности, место рождения, годы рождения и смерти (если человек
#умер), вычислить возраст на данный момент (или момент смерти). Для хранения
#всех необходимых данных требуется использовать переменные. После вывода
#информации программа должна дожидаться пока пользователь нажмет Enter для
#выхода.

# Badmaeva M.N.
# 12.10.2016

print("Джон Гриффит Лондон более известен как американский писатель Джек Лондон")
place = "Сан-Франциско"
print("Место рождения: ",place)
birth = 1876
death = 1916
print("Годы жизни: ",birth, " - ",death)
interest = "Литература"
did = death - birth
print("Умер в ",did)
print("Интересы: ", interest)
input("\n\nНажмите Enter для выхода")