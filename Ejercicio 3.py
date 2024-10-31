import math

pi = math.pi

tolerancia = 1e-3

aproximación  = 0
n = 0

while abs(aproximación  - pi) >= tolerancia:
    n += 1
    termino1 = ((-1) ** (n + 1)) * ((1/5)**(2*n-1)) / (2 * n - 1)
    termino2=   ((-1) ** (n + 1)) * ((1/239)**(2*n-1)) / (2 * n - 1)
    aproximación  += 4*(4*termino1-termino2)
print("Número de términos necesarios: " + str(n))
print("Aproximación de pi:" + str(aproximación))
