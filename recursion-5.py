def myPow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        x = 1 / x
        n = -n
    half_pow = myPow(x, n // 2)
    if n % 2 == 0:
        return half_pow * half_pow
    else:
        return x * half_pow * half_pow


print(myPow(2.00000, 10)) 
print(myPow(2.10000, 3)) 
print(myPow(2.00000, -2)) 
