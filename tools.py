def is_prime(number:int):
    """find if prime boolean return"""
    if number == 2:
        return True
    if number<=1:
        return False
    for x in range(2,number):
        if number%x == 0:
            return False
        elif x*x > number:
            return True


def generator_fibonacci():
    """ fibonacci generator"""
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b
