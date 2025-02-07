def greet_improved(name):
    """
    Simple function printing: Hello + name
    :param name: the name of the person to greet
    :return: None
    """
    print("Hello", name)
    return None

greet_improved("John")

def custom_op(x=0, y=0):
    """
    Custom op: 10x + y
    :param x: the first number
    :param y: the second number
    :return: 10x + y
    """
    result = 10*x + y
    return result
print(custom_op(5,2))

x = custom_op(y=4, x=2)
print(f"The result is: {x}")


