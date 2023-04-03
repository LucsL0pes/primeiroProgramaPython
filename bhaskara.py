import math

a = float(input("insira o valor da a: "))
b = float(input("insira o valor de b: "))
c = float(input("insira o valor de c: "))

print(30 * "-")

delta = float((b ** 2) - 4*a*c)

if delta <= 0 or a == 0:
    print("Impossivel calcular")
else:
    resultado1 = float(-b + math.sqrt(delta))/(2*a)
    resultado2 = float(-b - math.sqrt(delta))/(2*a)
    print(f"R1 = {resultado1:.5f}")
    print(f"R2 = {resultado2:.5f}")
