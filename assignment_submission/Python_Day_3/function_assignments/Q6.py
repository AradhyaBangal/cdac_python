def toggle_case(ch):
    if ch.isupper():
        return ch.lower()
    elif ch.islower():
        return ch.upper()
    else:
        return ch  # for non-alphabet characters, return as it is

char_input = input("Enter a character: ")[0]  # take only the first character
result = toggle_case(char_input)
print("Toggled character:", result)
