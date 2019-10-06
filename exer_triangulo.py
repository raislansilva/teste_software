
def triangulo(lado1,lado2,lado3):
    value = None
    if lado1 > 99 or lado1 < 0 or lado2 >99 or lado2 < 0 or lado3>99 or lado3 <0:
        value = 0
    elif lado3 >= lado1+lado2  or lado2 >= lado1+lado3  or  lado1 >= lado2+lado3:
        if lado3 <= lado1-lado2  or lado2 <= lado1-lado3 or lado1 <= lado2-lado3:
            value = 4
    elif lado1 == lado2 and lado2 == lado3:
         value = 1
    elif lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado1 != lado3:
        value = 2
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        value = 3

    return value        
    
        

print(triangulo(10,10,10))

    



