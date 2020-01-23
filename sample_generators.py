def square(x):
    for i in x:
        yield i * i


x = [1, 2, 3, 4, 5]

store = square(x)
# print(next(store))
# print(next(store))
# print(next(store))
# print(next(store))
# print(next(store))

for i in store:
    print(i)
