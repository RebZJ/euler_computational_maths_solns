from tools import generator_fibonacci
import time

start = time.time()

f = generator_fibonacci()

sum = 0

for _ in range(4000000):
    num = next(f)

    if num >= 4000000:
        break

    if (num % 2 == 0):
        sum += num

end = time.time()

print("We found it boys:", sum)
print(end-start)
