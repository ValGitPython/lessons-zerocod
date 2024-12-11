# -*- coding: utf-8 -*-
print("Здравствуй!")
name=input("Как тебя зовут?")
print("Приятно познакомится",name)
age=int(input("Сколько тебе лет?"))
if (age<=7):
    print("Ты ходишь в садик!")
elif (age>7 and age<18):
    print("Ты ходишь в школу!")
else:
    print("Да ты уже взрослый!")