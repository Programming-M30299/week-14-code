def readFile(filename):
    try:
        inFile = open(filename, 'r')
        content = inFile.read()
        inFile.close()
        return content
    except FileNotFoundError:
        print("File not found")
        return None
    except PermissionError:
        print("Permission denied")
        return None


def getChoice():
    choice = input("Enter a number: ")
    while not choice.isdigit():
        print("That's not a number!")
        choice = input("Enter a number: ")
    choiceAsInt = int(choice)  # Can raise a `ValueError`
    return choiceAsInt
