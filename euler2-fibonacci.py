def fibonacci():
    list = [1, 2]
    number = 0
    evenTotal=2
    n = 0
    while list[n+1] < 4000000:
        number = list[n] + list[n+1]
        list.append(number)
        if number % 2 == 0:
            evenTotal += number
        n += 1

    print(evenTotal)
    print(list)

fibonacci()
