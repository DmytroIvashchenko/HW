from functools import reduce  # Використовується в 2-му завданні


# #  №1. Написати 3 приклади генераторних функцій з різними послідовностями.
def generator_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1


generator = generator_countdown(7)
print(next(generator))


# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


def degree_generator_function(n):
    for e in range(1, n):
        yield e ** e


result = degree_generator_function(4)
print(next(result))


# print(next(result))
# print(next(result))


def arithmetic_progression(x, d, size):
    count = 1
    while count <= size:
        yield x
        x += d
        count += 1


progression = arithmetic_progression(1, 2, 10)
print(next(progression))
for element in arithmetic_progression(1, 2, 10):
    print(element)


# #  №2. Написати свою реалізацію функції reduce() з описом в інлайнових та багаторядкових коментарях її роботи.
def my_reduce(a, b):
    c = a + b
    return c


print(reduce(my_reduce, [123, 345, 113]))  # реалізував reduce через задану попередньо функцію
print(reduce(my_reduce, [123, 345, 113], 100))  # reduce через задану попередньо функцію з додаванням 3-го аргументу

print(reduce(lambda a, b: a + b, [1, 3, 5, 6, 7, 8, 9, 10]))  # реалізував reduce через функцію lambda
print(reduce(lambda a, b: a + b, [1, 3, 5, 6, 7, 8, 9, 10], 10))


# # реалізував reduce через функцію lambda з додаванням 3-го аргументу
#
# """" Для використання функції reduce потрібно в дужках вказати функцію, яку має виконати reduce
#      та значення/ітеруємі об'єкти які мають виконати те що всередині заданої функції
#      функція reduce завжди повертає одне значення
#      ще є третій не обов'язковий аргумент, який стає першим агрументом для заданої функції """
#
#
# #  №3. Написати функцію яка за допомогою assert буде тестувати ваш самописний reduce
def my_reduce(a, b):
    assert b > 0, "B should be bigger than 0"  # наприклад ми хочемо щоб b був більший за 0.
    assert a < 0, "A should be lower than 0"  # наприклад ми хочемо щоб а був меньший за 0.
    c = a + b
    assert c != 0, "C should not be equal to 0"  # ми хочемо щоб с не дорівнював 0.
    return c


print(f'Result is {reduce(my_reduce, [-5, 10])}.')


#  №4. Створити клас із методом якого можна буде повертати область видимості створеного екземпляра класу.
class Visibility_detection:
    def __init__(self, name):
        self.name = name

    def visibility(self):
        if self in locals().values():
            return 'Object in locals visibility'
        else:
            return 'Object in globals visibility'


verification = Visibility_detection('test')
print(verification)
print(verification.visibility())
