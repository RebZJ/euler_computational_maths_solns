#problem 10 trivial solution
from tools import is_prime

sum = 0

for i in range(2000000):

    if is_prime(i) == True:
        sum += i

print(sum)
