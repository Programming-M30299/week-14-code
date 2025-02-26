def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print("File not found")
        return None
    except PermissionError:
        print("Permission denied")
        return None


def get_choice():
    choice = input("Enter a number: ")
    choice_as_int = 0
    while not choice.isdigit():
        print("That's not a number!")
        choice = input("Enter a number: ")
    choice_as_int = int(choice)  # Can raise a `ValueError`
    return choice_as_int
