"""P6E8 RAFA GIÓN version 1
Escribe un programa que te pida primero un número y luego te pida números
hasta que la suma de los números introducidos coincida con el número inicial.
El programa termina escribiendo la lista de números."""
#version en la que imprimimos el resultado a partir de la lista que hemos generado
num_ini=int(input("Dame un número"))
sumatorio=0
resultado=[]

while sumatorio<num_ini:
    num_a_sumar=int(input("Dime otro número"))
    if num_a_sumar+sumatorio<=num_ini:
        resultado.append(num_a_sumar)
        sumatorio+=num_a_sumar
        
print("El resultado de sumar ",end=" ")
for i in range(len(resultado)-1):
    print(resultado[i],end="+")

print(resultado[-1],"=",num_ini)

        
        
