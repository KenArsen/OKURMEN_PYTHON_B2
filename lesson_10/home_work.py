# 1 - тапшырма
"""
Консольдон ар бир (while) итерациясында бир сан киргизебиз(инпут менен). 
Эгерде 0 саны киргизилсе цикл бутуш керек. Жооп катары оң сандардын гана суммасын эсептеш керек. 
Эгерде терс сандар кезиккенде continue операторун колдонуу менен аны откоруп жибериниздер.

Мисалы:
2
-1
3
2
-5
7
0

Жооп:
14

Тушундурмо: 
2 + 3 + 2 + 7 бул сандар он сандар

"""
summa = 0
while True:
    number = int(input("Введите одно число: "))

    if number == 0:
        break
    elif number < 0:
        continue
    else:
        summa += number

print(f'Сумма = {summa}')


# 2 - тапшырма
"""
Программага бир int тибиндеги сан берилет. 
Анын маанисинен квадраты чон болгон биринчи санды табыныз (1ден баштап текшерип),
Программаны while циклин колдонуп ишке ашыруу керек.

Мисалы:
10

Жооп:
4

Тушундурмо: 
1 ** 2 = 1
2 ** 2 = 4
3 ** 2 = 9
4 ** 2 = 16 эн биринчи сан, квадраты ондон чон
"""

number = int(input("Введите одно число: ")) # 100
i = 1 
while number > i ** 2: # 100 > 10 ** 2 -> False
    i += 1 # i = 10
print(i)