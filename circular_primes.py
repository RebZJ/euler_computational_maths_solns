#project euler problem 35
from tools import is_prime
import time

start = time.time()
#converts from character array to int
def convert(s):
    new = ""
    for x in s:
        new += x
    return int(new)



def circular_right_prime(num):
    res = [x for x in str(num)]

    for i in range(len(res)):
        if is_prime(convert(res)) is True:

            a = res.pop(0)
            res.append(a)
        else:
            return False

    return True

count = 0
for i in range(2,1000000):
    if (i>2) and (i%2==0) :
        pass
    else:
        if circular_right_prime(i) is True:
            count +=1

end = time.time()
print(count )
print("time %f" % (end - start))
