1.	# Найти НОК двух чисел

# num1 = int(input("Введите первое число: ")) 
# num2 = int(input("Введите второе число: "))

# if num1 > num2: (num1, num2) = (num2, num1)

# nok = num2
# while (True):
#     if nok % num1 == 0 and nok % num2 == 0:
#         print(f'Наименьшее общее кратное для чисел {num1} и {num2} = {nok}')
#         break
#     else: nok += 1

#=========================== Задача2 ====================================

#2.	Вычислить число Пи c заданной точностью d
#   Пример: при d = 0.001,  c= 3.141. 
# Примечание: в следующем примере только вывод числа Пи, а не полноценное его вычисление.

# import math
# n =(input('Введите нужную точность: '))
# d = int(len(n))
# if d < 2: d = 2
# print (round(math.pi, d-2)) # Метод округляет последнюю цифру, и получается не совсем то что надо

# pi = str(math.pi)
# for i in range(d):
#     print(pi[i], end = '') # Выводим сторку нужной длинны.

#============================== Задача 3 =======================================

#3.	Составить список простых множителей натурального числа N

# num = int(input("Введите число: ")) 
# m_list =[]
# m = 2
# while num > 1:
#     if num % m == 0:
#         m_list.append(m)
#         num = num // m
#     else: m = m+1
#     if num <= m:
#         m_list.append(num)
#         break
# print(m_list)

#============================ Задача 4 ========================================

#4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#   Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# number_list = [1, 2, 3, 5, 1, 5, 3, 10]
# res_list = []
# res_list.append(number_list[0])
# for i in range(len(number_list)-1):
    
#     for j in range(i+1):
        
#         if number_list[i+1] == number_list[j]: break
#         if j == i: res_list.append(number_list[i+1])
    
# print(res_list)

#============================ Задача 5 ========================================

#  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

# with open('file.txt', 'w') as data:
#     data.write('1 2 7 3 2 4 5 6 7 8 0 9') # Записываем файл
# path = 'file.txt'
# data = open(path, 'r') # cчитываем файл
# for line in data:
#     print(line)
# data.close()

# num_list = list(map(int, line.split(" "))) # преобразуем строку в список
# res_list = ''
# for i in num_list:
#     if i % 2 != 0: res_list += str(i) + " " # записываем только нечётные числа
# print(res_list)

# with open('file.txt', 'w') as data:
#     data.write(str(res_list)) # Переписываем файл

