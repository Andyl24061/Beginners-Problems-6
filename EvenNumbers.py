def getEven(numbers):
    
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

numbers = list(map(int, input("Enter a list of integers: ").split()))

print(getEven(numbers))
