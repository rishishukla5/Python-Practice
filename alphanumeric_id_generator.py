import string
import random

store = []


def alphnumeric_random_value(n):
    for x in range(n):
        value = ""
        while True:
            for i in range(1):
                value += random.choice(string.ascii_letters + string.digits)
            if value not in store:
                yield value
                break
            else:
                value = ""


n = int(input("Enter the number of ids to be generated: "))

temp = alphnumeric_random_value(n)

for it in temp:
    store.append(it)
    print(it)
