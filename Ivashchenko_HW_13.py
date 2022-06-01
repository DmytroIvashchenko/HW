# class Counter:
#     def __init__(self, func):
#         self.func = func
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self.func(*args, **kwargs)
#
#
# @Counter
# def foo():
#     pass
#
#
# for i in range(10):
#     foo()
#
# print(foo.count)


class Car:
    def __init__(self, name='', wheels=4, weight=100):
        self.name = name
        self.wheels = wheels
        self.weight = weight

    @property
    def type_of_car(self):
        type_of_car = (self.wheels + self.weight) / 10
        if type_of_car > 40:
            print("It's a Crossover.")
        else:
            print("It's a passenger car.")
        return type_of_car

    @type_of_car.setter
    def type_of_car(self, value):
        self.type_of_car = value

    @type_of_car.deleter
    def type_of_car(self):
        self.type_of_car = 'not identefication'

    @classmethod
    def car_validate(cls, car):
        assert isinstance(car, cls)
        if 100 > car.weight > 0:
            return "It's okay, you don't need an inspection."
        return 'Please go to the technical inspection.'

    @staticmethod
    def colour_of_car(colour):
        colour = 'White'
        return f'Colour is {colour}.'

    def __repr__(self):
        return f"Car is {self.name}."


mers = Car('Mercedes', 4, 80)
print(mers)
print(mers.type_of_car)
print(mers.colour_of_car(mers))
print(mers.car_validate(mers))
