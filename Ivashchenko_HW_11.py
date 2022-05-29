#  №2. Скинути файл з прикладами всіх конструкцій try:except:else:finally.
my_dict = {"a": 1, "b": 2}
try:
    value = my_dict["с"]
except KeyError:
    print("That key does not exist!")
finally:
    print("Finally!!!")

my_list = [1, 2, 3, 4, 5]

try:
    my_list[2]
except IndexError:
    print("That index is not in the list!")
else:
    print('Its okay')


#  №3. Написати функцію, яка приймає від користувача 2 аргументи і ділить один на інший.
def division_operation(x, y):
    try:
        result = x / y
        print(f'Division result is {result}')
        return result
    except ZeroDivisionError:
        print('ай яй яй делить на ноль можно не многим')
    except Exception as ex:
        print(ex)
    finally:
        print("I am happy that you learn python")


print('Argument is 4 and 1.')
div_one = division_operation(4, 1)
print("Argument is 'adafaf' and 3.")
div_two = division_operation('adafaf', 3)
print('Argument is 3 and 0.')
div_three = division_operation(3, 0)
