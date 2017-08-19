#Programa para convertir de Celsius a Fahrenheit o viceversa
#Creado por @neriphy

print("Si desea convertir Celsius a Fahrenheit introduzca 1 ")
print("Si desea convertir Fahrenheit a Celsius introduzca 2 ")
convertir_a = int(input())

if convertir_a == 1:
    grados = int(input("Introduzca los grados Celsius "))
    resultado = (grados * 1.5) + 32
    print(grados,"grados Celsius, serian",resultado,"grados Fahrenheit")

if convertir_a == 2:
    grados = int(input("Introduzca los grados Fahrenheit "))
    resultado = (grados  - 32) / 9/5
    print(grados,"grados Fahrenheit, serian",resultado,"grados Celsius")
