import math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui uma única raiz real: x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}")


bhaskara(1, -5, 6)