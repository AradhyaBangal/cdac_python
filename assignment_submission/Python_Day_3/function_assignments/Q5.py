def check_number(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

number = int(input("Enter a number: "))
result = check_number(number)
print("Result:", result)