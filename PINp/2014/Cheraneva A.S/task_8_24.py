#Задача №8. Вариант 24.

#Доработать игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка. 
#Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. 
#Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, 
#получали больше тех, кто запросил подсказку.

#Cheraneva A.S.
#30.05.2016

import random
WORDS=("компьютер","монитор","мышь","клавиатура","коврик","наушники")
word=random.choice(WORDS)
correct=word
jumble=""
hint=""
ball=100
while word:
	position=random.randrange(len(word))
	jumble+=word[position]
	word=word[:position]+word[(position+1):]

print(
"""
		Добро пожаловать в игру 'Анаграмма'!
	Надо переставить буквы так, чтобы получилось осмысленное слово.
(Для выхода нажмите Enter, не вводя своей версии.)
"""
)
print ("Вот анаграмма:", jumble)
guess=" "
while guess !=correct and guess!="":       
	guess=input("Попробуйте отгадать исходное слово: ")
	if guess=="подсказка":
		hint= (correct[:position+1])
		print (hint)
		ball-=10
		position+=1
	elif guess==correct:
		print("Да, именно так! Вы отгадали!\n")
		print ("Ваши баллы",ball)
	elif guess!=correct:
		print("Неправильно, попробуй еще раз.")
print("Спасибо за игру.")
input("Нажмите Enter для выхода.")
