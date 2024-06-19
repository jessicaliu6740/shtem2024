def fibonacci(num):
    counter = 0
    first = 1
    second = 1
    while counter <= num:
        print(first, end=" ")
        temp = second
        second = first + temp
        first = temp
        counter += 1

fibonacci(6)