#Ejercicio 2

numero1 = int(input("Escriba un numero"))
numero2 = int(input("Escriba un numero"))

if numero1%2==0 and numero2%2==0:
    print("Ambos son pares")
elif numero1%2==0 and numero2%2!=0:
    print(f"{numero1} es par")
elif numero1%2!=0 and numero2%2==0:
    print(f"El numero 2 no es par")
else:
    print("Ambos numeros son impares")



