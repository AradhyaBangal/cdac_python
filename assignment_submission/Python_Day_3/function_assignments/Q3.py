def display_values(char, num, text):
    print("Character:", char)
    print("Integer:", num)
    print("String:", text)

char_input = input("Enter a character: ")[0]    # Takes first character only
num_input = int(input("Enter an integer: "))
text_input = input("Enter a string: ")

display_values(char_input, num_input, text_input)
