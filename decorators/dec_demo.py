def swap_dec(fn):
    def wrapper(n1,n2):
        if n1<n2:
            n1,n2=n2,n1
        return fn(n1,n2)
    return wrapper


def round_dec(fn):
    def wrapper(num1,num2):
        num1=round(num1)
        num2=round(num2)
        return fn(num1,num2)
    return wrapper


@round_dec
@swap_dec
def addition(num1,num2):
    return num1+num2

@round_dec
@swap_dec
def substration(num1,num2):
    return num1-num2

@round_dec
@swap_dec
def division(num1,num2):
    return num1/num2

@round_dec
@swap_dec
def products(num1,num2):
    return num1*num2


print(substration(2.6,10.1))
print(division(10,3.5))
print(addition(8.2,2.3))
print(products(2.6,3.8))
