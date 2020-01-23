import time


def outer_function(original_function):
    def inner_function(*argument1, **argument2):
        start = time.time()
        print("Start Time: " + str(start))
        original_function(*argument1, **argument2)
        end = time.time()
        print("End Time: " + str(end))
        print("Time Taken: " + str(end - start))

    return inner_function


@outer_function
def original_function(x):
    print("Printing value: "+ str(x))


original_function("Hi")