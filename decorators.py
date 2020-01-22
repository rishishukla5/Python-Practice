def square(x):
    return x * x


def list_square(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


def get_val(func, x):
    def print_val(val):
        print(val)

    print_val(func(x))


def logger(msg):
    def log():
        print(msg)

    return log()


squares = list_square(square, [1, 2, 3, 4, 5])

get_val(square, 8)

log_hi = logger('Hi')

log_hi()

print(squares)
