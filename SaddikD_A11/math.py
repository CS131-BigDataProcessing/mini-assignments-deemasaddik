def power(a,b):
  return a ** b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
