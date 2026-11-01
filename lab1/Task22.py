def type_check(*types):
    def dec(func):
        def w(*args):
            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError("error type")
            result = func(*args)
            return result
        return w
    return dec

@type_check(int, int)
def add(x, y):
    print(x + y)

add(2, "ggggg")