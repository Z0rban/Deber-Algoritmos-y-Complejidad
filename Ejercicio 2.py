import cmath

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b + (delta**0.5)) / (2 * a)
    x2 = (-b - (delta**0.5)) / (2 * a)
elif delta == 0:
    x1 = x2 = -b / (2 * a)
else:
    parte_real = -b / (2 * a)
    parte_imaginaria = (abs(delta)**0.5) / (2 * a)
    x1 = complex(parte_real, parte_imaginaria)  
    x2 = complex(parte_real, -parte_imaginaria) 
print("Raíz 1 (x1):", x1)
print("Raíz 2 (x2):", x2)
