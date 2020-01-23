store = dict()


def outer_function(original_function):
    def inner_function(*arguement1):
        temp = (str(original_function), arguement1)
        if temp in store:
            print("Cached value: " + str(store[temp]))
        else:
            store[temp] = original_function(*arguement1)
            print("Value added to cache: " + str(store[temp]))

    return inner_function


@outer_function
def original_function(x):
    return x + 1


@outer_function
def second_function(x1, x2):
    return x1 + x2


original_function(1)
original_function(1)
original_function(2)
second_function(1, 2)
original_function(2)
second_function(1, 2)
