def find_palin(num):
    s = str(num)
    if (int(s[ : : -1]) == num):
        return True
    else:
        return False

def palin_generator():
    palin_list = []
    for i in range(999,900-1):
        for a in range(999,900,-1):
            if find_palin(a * i) == True:
                palin_list.append(a * i)
    return palin_list

def largest_num(list):
    num = 0
    for i in list:
        if num < i:
            num = i
    print(num)
    return(num)

largest_num(palin_generator())
