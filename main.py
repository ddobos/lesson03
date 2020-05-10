print('lesson03')


def inputValue():
    print('Please write a number:')
    a = 0
    while (True):
        try:
            a = int(input())
            if (a < 0):
                print('Error input a number, \n number was by positive')
            else:
                break
        except ValueError:
            print('Error input a number, try again')
    return a


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