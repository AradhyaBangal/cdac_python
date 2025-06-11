def take_chars(c1, c2, c3, c4='', c5=''):
    all_chars = c1 + c2 + c3 + c4 + c5
    return all_chars

user_input = input("Enter 3 to 5 characters: ")

if 3 <= len(user_input) <= 5:
    result = take_chars(*user_input)
    print("Result:", result)
else:
    print("Invalid input. Please enter between 3 and 5 characters.")