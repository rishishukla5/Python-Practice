def total_sum(*integers):
    result = 0
    for i in integers:
        result += i
    return result


def concatenate(**words):
    result_string = ''
    for i in words.values():
        result_string += i
        result_string += ' '
    return result_string


result = sum((1, 2, 3))
result_string = concatenate(a="This", b="is", c="Amazing")

print(result)
print(result_string)
