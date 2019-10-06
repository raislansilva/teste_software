
def triangulo(lado1,lado2,lado3):
    if lado1 > 99 or lado1 < 0 or lado2 >99 or lado2 < 0 or lado3>99 or lado3 <0:
        return 0
    elif lado3 >= lado1+lado2  or lado2 >= lado1+lado3  or  lado1 >= lado2+lado3:
        if lado3 <= lado1-lado2  or lado2 <= lado1-lado3 or lado1 <= lado2-lado3:
            return 4
    elif lado1 == lado2 and lado2 == lado3:
        return 1
    elif lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado1 != lado3:
        return 2
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        return 3    
    
        

print(triangulo(10,10,10))

    



