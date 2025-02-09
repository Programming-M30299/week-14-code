def wc(filename):
    with open(filename, 'r') as f:
        text = f.read()
    number_of_characters = len(text)
    list_of_words = text.split()
    number_of_words = len(list_of_words)
    number_of_lines = text.count('\n')
    return number_of_characters, number_of_words, number_of_lines


def main():
    filename = input("Enter the name of the file: ")
    chars, words, lines = wc(filename)
    print(f"Characters: {chars}, Words: {words}, Lines: {lines}")


main()
