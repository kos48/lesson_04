'''5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
произведения всех элементов списка.
Подсказка: использовать функцию reduce()'''

from functools import reduce

def my_f(num_1, num_2):
    return num_1 * num_2

my_list = [number for number in range(100, 1001) if number %2==0]

print(reduce(my_f, my_list))

#5
