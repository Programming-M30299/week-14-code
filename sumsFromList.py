def sumList(numbers, count):
    total = 0
    for i in range(count):
        total += numbers[i]
    return total


def getNumber():
    number = int(input("Enter a number: "))
    return number


def main():
    numbers = []
    while True:
        print("Enter a non-negative number to add to the list.")
        print("Or enter a negative number to stop.")
        number = getNumber()
        if number >= 0:
            numbers.append(number)
        else:
            break

    while True:
        print("Enter many numbers from the list would you like to sum up.")
        print("Or enter a negative number to stop.")
        count = getNumber()
        if count >= 0:
            total = sumList(numbers, count)
            print(f"The sum of the first {count} numbers is {total}")
        else:
            break


main()
