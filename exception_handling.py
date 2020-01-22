result = None

a = float(input("First Number : "))
b = float(input("Second Number : "))

try:
    result = a / b

except ZeroDivisionError as e:
    print('Error = ', e)
except TypeError as e:
    print('Error', e)
else:
    print('__else__')
finally:
    print('__finally__')

print("Result : " + str(result))
