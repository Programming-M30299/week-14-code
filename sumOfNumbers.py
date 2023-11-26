def sumOfList(numbers, length):
    total = 0
    if length == 0:
        return 0
    else:
        for i in range(length):
            number = float(numbers[i])
            total += number
        return total


def getNumber():
    number = float(input("Enter a number: "))
    return number


def main():
    numbers = []
    while True:
        print("Enter a positive number to add to the list or a negative number to stop.")
        number = getNumber()
        if number >= 0:
            numbers.append(number)
        else:
            break
    print("Enter the total number of numbers in the list.")
    count = getNumber()
    total = sumOfList(numbers, count)
    print("The sum of the numbers in the list is", total)


main()
