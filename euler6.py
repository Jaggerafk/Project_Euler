def sums_squares(num):
    sums_square = 0
    for i in range(1,num+1):
        sums_square += (i * i)
    return(sums_square)

def square_sum(num):
    square_sum = 0
    for i in range(1,num+1):
        square_sum += i
    square_sum = square_sum**2
    print (square_sum)
    return square_sum - sums_squares(num)

print(square_sum(100))
