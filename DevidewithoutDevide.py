def divide(dividened, divisor):
    
    sign = -1 if (dividened < 0) ^ (divisor  < 0) else 1
    dividened = abs(dividened)
    divisor = abs(divisor)
    quotient = 0
    temp = 0
    
    for i in range(31, -1, -1):
        if temp + (divisor<<i) <= dividened:
            temp += divisor<< i
            quotient |= 1 << i
    if sign == -1:
        quotient = -quotient
            
    return quotient
    
a = int(input("Enter a for a/b = "))
b = int(input("Enter b for a/b = "))

print("result of",a, "/", b, "=", divide(a, b))