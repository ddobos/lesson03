print('lesson03')


def inputValue():
    print('Please write a number:')
    while True:
        try:
            a = int(input())
            if a < 0:
                print('Error input a number, \n number must be positive')
            else:
                return a
        except ValueError:
            print('Error input a number, try again')


def multiple(firstValue, secondValue):
    return firstValue * secondValue


def divide(firstValue, secondValue):
    try:
        return firstValue / secondValue
    except ZeroDivisionError:
        print('division by zero')


print('Please input first value')
firstValue = inputValue()

print('Please input second value')
secondValue = inputValue()

print('multiply result is: {}'.format(multiple(firstValue, secondValue)))
print('divide result is: {}'.format(divide(firstValue, secondValue)))


def sum(firstValue, secondValue):
    return firstValue + secondValue


def diff(firstValue, secondValue):
    return firstValue - secondValue


print('Pleas input first value')
firstValue = inputValue()

print('Pleas input Second value')
secondValue = inputValue()

print('sum value: {}'.format(sum(firstValue, secondValue)))
print('difference value: {}'.format(diff(firstValue, secondValue)))