"""
2. Desarrollar un programa que permita almacenar las edades de un grupo de 10 personas en un
vector de enteros y luego determine la cantidad de personas que son menores de edad, mayores
de edad, cuántos adultos mayores, la edad más baja, la edad más alta y el promedio de edades
ingresadas. Para el ejercicio anterior, suponga que un adulto mayor debe tener una edad igual o
superior a 60. Debe validar para cada ingreso, que los valores estén en un rango entre 1 y 120 años.
En caso de error deberá notificar y solicitar un nuevo valor.




"""
vector = []

for i in range(10):
    while True:
        valor = int(input(f"Ingrese la edad de la persona {i+1}: "))
        if 1 <= valor <= 120:
            vector.append(valor)
            break
        else:
            print(" Valor no válido. es  1 y 120 años.")


mayor = max ( vector )

menor = min (vector )

promedio = sum (vector)/ len (vector )

mayoresA60 = [x for x in vector if x >= 60]
cantidadMayoresA60 = len(mayoresA60)

menoresDeEdad  = [x for x in vector if x  < 18 ]
cantidadMenoresDeEdad = len(menoresDeEdad)

mayorEdad = [x for x in vector if x >= 18]
cantidadMayorEdad = len(mayorEdad)

print ( "la edad más baja es : ", menor)
print ( "la edad más alta  es : ", mayor )
print ( "el promedio  es : ", promedio)
print ( "las personas mayores a 60 son  : ", cantidadMayoresA60)
print ( "las personas mayores de edad  son  : ", cantidadMayorEdad)
print ( "las personas menores  de edad  son  : ", cantidadMenoresDeEdad)

