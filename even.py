def is_even(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False

def is_odd(is_even):
    if is_even != True:
        return "odd"
    else:
        return is_even

print(is_odd(is_even(42)))
    

