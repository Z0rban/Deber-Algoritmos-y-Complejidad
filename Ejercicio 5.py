a = [1, 2, 3, 4, 5] 
b = [6, 7, 8, 9, 10]  
n = len(a) 

def suma_doble(a,b,n):
    suma_total = 0

    for i in range(n):
        for j in range(i + 1):
            suma_total += a[i] * b[j]

    print("La suma doble es:", suma_total)

def suma_doble_optimizada(a,b,n):
    suma_acumulada_a = [0] * n
    suma_acumulada_a[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        suma_acumulada_a[i] = suma_acumulada_a[i + 1] + a[i]
    suma_total = 0
    for j in range(n):
        suma_total += b[j] * suma_acumulada_a[j]

    print("La suma doble optimizada es:", suma_total)

suma_doble(a,b,n)
suma_doble_optimizada(a,b,n)