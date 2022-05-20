# Функции all,any,filter №1
x = name, age = input('Please fill your name and age').split()
name == 'Dima'
age = int(age) == 25
y = list(filter(str.isdigit, x))
print(y)
print(all([name, age]))
print(any([name, age]))

# Функции all,any,filter №2
price = budget, car = input('Please enter your budget and the car you want to buy').split()
budget = int(budget) == 5000
car == 'Volkswagen' or 'Opel' or 'Skoda' or 'Chevrolet'
money_price = list(filter(str.isdigit, price))
print(f'{money_price[0]} is good amount to buy car')
print(all([budget, car]))
print(any([budget, car]))

# Функции all,any,filter №3
marks = input('Please fill up marks')
marks_split = Ivanov, Petrov, Sidorov, Dmitrov, Khomenko = marks.split()
marks = [int(Ivanov), int(Petrov), int(Sidorov), int(Dmitrov), int(Khomenko)]
mark = list(filter(lambda x: x % 2 == 0, marks))
print(mark)
Ivanov = int(Ivanov) == 3
Petrov = int(Petrov) == 4
Sidorov = int(Sidorov) == 4
Dmitrov = int(Dmitrov) == 5
Khomenko = int(Khomenko) == 2
print(all([Ivanov, Petrov, Sidorov, Dmitrov, Khomenko]))
print(any([Ivanov, Petrov, Sidorov, Dmitrov, Khomenko]))

#  Рекурсия 1 вывод числа с максимальным значением из списка чисел
def GetMaxList(L):
    if len(L) > 1:
        max = GetMaxList(L[1:])
        if L[0] < max:
            return max
        else:
            return L[0]
    if len(L) == 1:
        return L[0]


L = [2, 5, 8, 11, 3]
res = GetMaxList(L)
print("res = ", res)


#  Рекурсия 2 возведение числа x в степень y
def Power(x, y):
    if y > 0:
        return x * Power(x, y - 1)
    else:
        return 1


x = 5
y = 7
res = Power(x, y)
print("res = ", res)


#  Рекурсия 3 нахождение суммы чисел списка
def CalcSumNumbers(A):
    if A == []:
        return 0
    else:
        result_sum = CalcSumNumbers(A[1:])
        result_sum = result_sum + A[0]
        return result_sum


list_of_numbers = [0, 5, 9, 21, 9, 1]
result_sum = CalcSumNumbers(list_of_numbers)
print("summ = ", result_sum)


#  decorator 1
# def decorator1(func):
#     def new_func(n):
#         return func(n) + '₴'
#
#     return new_func
#
#
# @decorator1
# def myfunction(a):
#     return a
# print(myfunction('50'))

#  decorator 2
# def decorator1(function):
#     def wrapper():
#         print('this is first message')
#         function()
#         print ('this is second message')
#     return wrapper
# def decorator2():
#     print('this is third message')
# decorator2 = decorator1(decorator2)
# decorator2()

#  decorator 3
def decorator1(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


def decorator2uppercase(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@decorator1
@decorator2uppercase
def say_hi():
    return 'python is good language'


print(say_hi())