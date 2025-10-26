print(" 1: ( calcular area )")
print(" 2: ( calcular perimetro )")
opcion =  int (input ( "escriba la opcion : "))
print("Elige una figura para calcular área y perímetro:")
print("1: Rectángulo")
print("2: Triángulo escaleno")
print("3: Cuadrado")
print("4: Círculo")

figura  =  int  (input ( "figura:  "))


#AREAS

#RECTANGULO 
if opcion == 1 and figura == 1:
    base  =  float (input ( "escriba la base  : "))
    altura  =  float (input ( "escriba la altura  : "))
    resultado = base * altura 
    print ( "el resultado es:", resultado  )

#TRIANGULO 
elif opcion == 1 and figura == 2:
    
    
    a = float(input("ingrese Lado a: "))
    b = float(input("ingrese Lado b: "))
    c = float(input("ingrese Lado c: "))

    
    subarea= (a + b + c) / 2

    
    area = (subarea * (subarea - a) * (subarea - b) * (subarea - c))**0.5
    print(f"El área del triángulo es: {area:.2f}")

#CUADRADO
elif  opcion == 1 and figura == 3:
    lado =  float (input ( "escriba el lado   : "))
    resultadoC= lado**2
    print ( "el resultado es:", resultadoC  )

#CIRCULO 
elif  opcion == 1 and figura == 4:
    radio =  float (input ( "escriba el radio   : "))
    resultado_circulo = 3.1416 * (radio **2 )
    print ( "el resultado es:", resultado_circulo  )



#PERIMETROS 

#RECTANGULO 
elif  opcion == 2 and figura == 1:
    basePer  =  int (input ( "escriba la base  : "))
    alturaPer  =  int (input ( "escriba la altura  : "))
    resultadoPer = 2 * (basePer + alturaPer) 
    
    print ( "el resultado es:", resultadoPer  )

#TRIANGULO 

elif  opcion == 2 and figura == 2:
    aPer = float(input("ingrese Lado a: "))
    bPer = float(input("ingrese Lado b: "))
    cPer = float(input("ingrese Lado c: "))

    
    subareaPer= (aPer + bPer + cPer)
    print ( "el resultado es:", subareaPer )

#CUADRADO 
elif  opcion == 2 and figura == 3:
    
    ladoPer =  float (input ( "escriba el lado   : "))
    resultadoCPer= 4 * ladoPer
    print ( "el resultado es:", resultadoCPer )

# CIRCULO 
elif  opcion == 2 and figura == 4:
    radioPer =  float (input ( "escriba el radio   : "))
    resultado_circulo_perimetro = (2* 3.1416) * radioPer
    print ( "el resultado es:", resultado_circulo_perimetro  )

else:
    print ("valor no valido")