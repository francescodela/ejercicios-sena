"""
3. Escriba un programa que lea dos vectores de números enteros ordenados ascendentemente y
luego produzca la lista ordenada de la mezcla de los dos, por ejemplo, si los dos arreglos tienen los
números 1 3 6 9 17 y 2 4 10 17, respectivamente, la lista de números en la pantalla debe ser 1 2 3 4
6 9 10 17 17. Limite los vectores a un tamaño de 5 y debe validar en cada ingreso que realmente se
estén ingresando los datos de forma ascendente.

"""
# Leer el primer vector
while True:
    try:
        vector1 = list(map(int, input("Ingrese 5 números del primer vector (orden ascendente): ").split()))
        if len(vector1) != 5:
            print("Debe ingresar  5 números  ")
            continue
        if all(vector1[i] <= vector1[i+1] for i in range(4)):
            break
        else:
            print("Los números no están en orden ascendente. Inténtelo de nuevo.")
    except ValueError:
        print("Debe ingresar solo números enteros.")


while True:
    try:
        vector2 = list(map(int, input("Ingrese 5 números del segundo vector (orden ascendente): ").split()))
        if len(vector2) != 5:
            print("Debe ingresar  5 números.")
            continue
        if all(vector2[i] <= vector2[i+1] for i in range(4)):
            break
        else:
            print("Los números no están en orden ascendente ")
    except ValueError:
        print("tiene que  ingresar solo números enteros  ")


mezcla = sorted(vector1 + vector2)


print("La lista ordenada es:")
print(mezcla)
