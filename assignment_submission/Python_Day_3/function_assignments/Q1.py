def add():
    print("Addition of 2 numbers")
def modify():
    print("modify the inputs")
def delete():
    print("Delete the inputs")

try:
    choice = int(input("Enter 1 (add), 2 (modify), or 3 (delete): ").strip())
except ValueError:
    print("Please enter a valid integer (1, 2, or 3).")
else:
    match choice:
        case 1:
            add()
        case 2:
            modify()
        case 3:
            delete()
        case _:
            print("Invalid option—choose 1, 2, or 3.")