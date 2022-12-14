def decorator_function (function):
    def wrapper_function(*args):
        print("hello")
        function(args[0])
        print("bye")
    return wrapper_function


@decorator_function
def say_hi(name):
    print(f"hello World{name}")


say_hi('tony')