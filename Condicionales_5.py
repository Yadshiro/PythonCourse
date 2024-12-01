#Ejercicio 5
numero_1 =float(input("Ingrese un numero"))
numero_2 =float(input("Ingrese un numero"))

operacion = input("Digite la Operacion").upper()

if operacion=="S":
    suma = numero_1+numero_2
    print(f"\nLa suma es: {suma}")
elif operacion=="R":
    resta= numero_1-numero_2
    print(f"\nLa resta es: {resta}")
elif operacion=="M":
    multiplicacion= numero_1*numero_2
    print(f"\nLa multiplicacion es: {multiplicacion}")
elif operacion=="D":
    division= numero_1/numero_2
    print(f"\nLa division es: {division:.2f})")
else:
    print("\nEsta incorrecta la operacion")

    