# project euler problem 46

from tools import is_prime
import time

large_num = 100000

start = time.time()


def is_composite_odd(x):
    if (is_prime(x) is False) and (x % 2 != 0):
        return True
    else:
        return False


prime_list = []
square_list = [2]


for x in range(2, large_num):

    square_list.append(2*x*x)

    if is_prime(x) is True:
        prime_list.append(x)

    if is_composite_odd(x) is True:

        found: bool = True
        # check if it's a prime + twice the square of any number
        for prime in prime_list:
            if prime > x:
                break
            for square in square_list:

                if (square + prime == x):

                    found = False
                    break
                if square > x:
                    break

        if found is True:
            print("We found it boys:", x)
            break

        found = True

end = time.time()
print(end - start)
