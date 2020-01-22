import time


def outer_function(original_function):
    def inner_function():
        start = time.time()
        print("Start Time: " + str(start))
        original_function()
        end = time.time()
        print("End Time: " + str(end))
        print("Time Taken: " + str(end - start))
    return inner_function()


@outer_function
def original_function():
    print("This is the original function")