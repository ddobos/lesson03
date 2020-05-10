print('lesson03')


def inputValue():
    print('Please write a number:')
    while True:
        try:
            a = int(input())
            if a < 0:
                print('Error input a number, \n number was by positive')
            else:
                return a
        except ValueError:
            print('Error input a number, try again')