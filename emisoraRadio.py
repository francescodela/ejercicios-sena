"""


4. Una emisora con presencia en diferentes ciudades, desea conocer el rating de canciones y
cantantes más escuchados (sonados) en este semestre del año. Por lo tanto, se ha pedido a
10
aprendices del SENA desarrollar una solución que permita conocer la respuesta de 6 personas con
relación a sus gustos musicales. Con fines administrativos y realizar una rifa entre las personas
encuestadas, la emisora desea poder registrar de las personas entrevistadas su nombre, número de
identificación (cédula), fecha de nacimiento, correo electrónico, ciudad de residencia, ciudad de
OM
origen, Además, se deberá poder almacenar el artista y titulo de hasta 3 canciones favoritas en
cada una de las personas que se ingrese. Teniendo en cuenta lo anterior, se sugiere que la solución
deberá mostrar un menú que permita las siguientes opciones:
F
AR
a. Agregar una persona con los datos que se listan anteriormente.
b. Mostrar la información personal de una persona particular por medio de su posición en el
vector


"""
print("1: Añadir persona")
print("2: Ver persona")

personas = []
opcion = int(input("Ingrese la opción: "))

if opcion == 1:
    for i in range(6):
        print(f" Registro de persona {i+1} ")
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        fecha = input("Fecha de nacimiento: ")
        correo = input("Correo electrónico: ")
        ciudad_residencia = input("Ciudad de residencia: ")
        ciudad_origen = input("Ciudad de origen: ")

        canciones = []
        for j in range(3):
            print(f"\nCanción {j+1}:")
            artista = input("  Artista: ")
            titulo = input("  Título: ")
            canciones.append({"artista": artista, "titulo": titulo})

        persona = {
            "nombre": nombre,
            "cedula": cedula,
            "fecha_nacimiento": fecha,
            "correo": correo,
            "ciudad_residencia": ciudad_residencia,
            "ciudad_origen": ciudad_origen,
            "canciones": canciones
        }

        personas.append(persona)

elif opcion == 2:
    print("Escoge quién (1-6)")
    numeroPersona = int(input("Ingrese el número: "))
    if numeroPersona <= len(personas):
        print(personas[numeroPersona - 1])
    else:
        print(" no existe")







    