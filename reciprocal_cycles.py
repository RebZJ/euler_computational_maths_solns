#problem 26
def long_division_one(num):
    array_return = []
    remainder_list = []
    initial  = 1

    #to not count 0's in the beginning
    first_run = True
    while True:
        if initial<num:
            initial = initial *10

            if first_run ==False:

                if initial<num:
                    array_return.append(0)

        else:
            first_run = False

            remainder = initial%num
            quo = int((initial - remainder)/num)

            if remainder in remainder_list:
                return array_return

            remainder_list.append(remainder)
            array_return.append(quo)

            initial = remainder

            if remainder == 0:
                return array_return

largest = {'size':0,'number':0}

for i in range(1,1000):

    size = len(long_division_one(i))

    if size > largest['size']:
        largest['size'] = size
        largest['number'] = i

print(largest)
