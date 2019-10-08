# -*- coding: utf-8 -*-
def triangulo(a,b,c):
    value = None
    if type(a) == int and type(b) == int and type(c) == int and a in range(0,99) and b in range(0,99) and c in range(0,99):
        if c >= a+b  or b >= a+c  or  a >= b+c:
            if c <= a-b  or b <= a-c or a <= b-c:
                value = 4
        elif a == b and b == c:
            value = 1
        elif a != b and b != c and a != c:
            value = 3
        else:
            value = 2
    else:
        value = 0
                   

    return value        
    
        

print(triangulo(20,20,20))

    



