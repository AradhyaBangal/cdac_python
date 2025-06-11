def toggle_string(text: str) -> str:
    return text.swapcase()

user_input = input("Enter a string to toggle: ")
toggled = toggle_string(user_input)
print("Toggled string:", toggled)
