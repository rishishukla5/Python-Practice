import time


def outer_function(original_function):
    def inner_function(x):
        start = time.time()
        print("Start Time: " + str(start))
        original_function(x)
        end = time.time()
        print("End Time: " + str(end))
        print("Time Taken: " + str(end - start))

    return inner_function


@outer_function
def original_function(x):
    print("Printing value: " + str(x))


original_function(1)
