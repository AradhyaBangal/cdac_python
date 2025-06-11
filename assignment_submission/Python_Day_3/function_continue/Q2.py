def outer(x):
    """Outer function that defines and uses an inner (nested) function."""

    def inner(y):
        return x + y
    # Call inner from inside outer
    print("Result inside outer:", inner(5))  
    return inner

x_val = int(input("Enter value for outer function (x): "))
y_val = int(input("Enter value for inner function (y): "))

inner_function = outer(x_val)      # prints result inside outer
print("Result outside outer:", inner_function(y_val))