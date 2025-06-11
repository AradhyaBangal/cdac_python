def show1():
    print("Inside show1")

def show2():
    print("Inside show2")

def show3():
    print("Inside show3")

def caller(func):
    """Accepts another function and invokes it."""
    func()         # call the function that was passed in

# demo
caller(show1)   # → Inside show1
caller(show2)   # → Inside show2
caller(show3)   # → Inside show3
