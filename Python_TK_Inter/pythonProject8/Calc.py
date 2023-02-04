

def add(x , y):
    """ add funtion"""
    return x + y

def substract(x , y):
    """ substract function"""
    return x - y

def mutipl(x , y):
    """ multiply function """
    return  x * y

def divide(x , y):
    """ divide function """
    if y == 0:
        return  ValueError("Can not divide bei zero")
    return x / y

print(add(5 , 10))