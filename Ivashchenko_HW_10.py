#   Задання 0. Повторити код замикання, який був зроблен в відео.
def one():
    x = ['one', 'two']

    def inner():
        print(x)
        print(id(x))

    return inner


o = one()


#  Завдання 1. Функція, яка додає код країни до номера телефону.
def phone():
    user_phone = input('Fill up your phone number')

    def user():
        code_of_country = '+044'
        user_phone_with_code_of_country = code_of_country + user_phone
        return user_phone_with_code_of_country

    return user


result = phone()


#   Завдання 2. Написати функцію, яка бере в будь-якому виді об'єкт Python, виводить всі немагічні медоти в списку
# та декоратор що буде виводити кількість методів в об'єкті.
#   Завдання 3. Дописати декоратор, щоб він приймав аргумент, наприклад текст
def len_of_methods(arg):
    def methods(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result)
            len_methods = len(result)
            print(f"'{arg} {len_methods}'")
            return result

        return wrapper

    return methods


@len_of_methods('need to learn')
def methods_of_object(a):
    method_of_my_class = ([m for m in dir(type(a)) if not m.startswith('__')])
    return method_of_my_class


methods_of_object(tuple())


# Завдання 4. Створити декоратор для функції, яка приймає необмежену кількість позициційних ХЕШИРУЕМИХ об'єктів

# декоратор для кешировання
def cache_decorator(func):
    cache = {}

    def decorated_function(*args):
        print('-' * 50)
        print('args =', args)
        print('cache =', cache)
        if cache.get(args):
            print('Operation: get the result from the cache')
            return cache[args]
        else:
            print('Operation: calculating and caching the result')
            cache[args] = func(*args)
            return cache[args]

    return decorated_function


# приклад використання
@cache_decorator
def custom_sum(*args):
    return sum(args)


# результат
print('result =', custom_sum(1, 2))
print('result =', custom_sum(1, 2))
print('result =', custom_sum(1, 2, 3))
print('result =', custom_sum(1, 2, 3))
