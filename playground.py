def add(*args):
    print(args[-1])
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(2, 5, 8, 9, 20))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Toyota", model="Prius")
print(my_car.model)

