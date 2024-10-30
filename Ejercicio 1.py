import math

pi = math.pi

tolerance = 1e-3 #Para el literal b cambiamos por 1e-10

aproximación  = 0
n = 0

while abs((4 * aproximación ) - pi) >= tolerance:
    n += 1
    termino = (-1) ** (n + 1) * ((1**(2*n-1)) / (2 * n - 1))
    aproximación  += termino
print("Número de términos necesarios: " + str(n))
print("Aproximación:" + str(aproximación))