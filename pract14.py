x = 0
while True:
    string = input("Enter a number: ")
    if string.isdigit():
        x = int(string)
        break
    print("Oops!  That was no valid number.  Try again...")
