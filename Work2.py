#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (f'Сумма цифр; {sum}')