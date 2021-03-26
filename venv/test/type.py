def test(*args):
    for arg in args:
        if (type(arg) == int):
            print('int')
        elif (type(arg) == str):
            print('str')

test(1, 'c', 3)