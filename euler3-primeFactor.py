def finding_prime(num):
    divider = 2
    list_of_prime = []
    while(divider <= num):
        while (num % divider != 0):
                divider += 1
        num = num/divider
        list_of_prime.append(divider)
    return list_of_prime

def finding_largest_num(list_of_prime):
    largest_num = 0
    for i in list_of_prime:
        if largest_num < i:
            largest_num = i
    return largest_num

print(finding_largest_num(finding_prime(600851475143)))
