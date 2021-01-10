def smallest_divisble_num():
    num = 2520
    value = False
    while value == False:
        num += 20
        for i in range(1,21):
            if (num % i == 0):
                value = True
            else:
                value = False
                break

    print(num)

smallest_divisble_num()
