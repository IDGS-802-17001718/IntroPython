print("Suma de numeros")

num1=int(input("Dame un valor de n1"))
num2=int(input("Dame un valor de n2"))

if num1>num2 :
    print("El {} es mayor que el {}".format(num1,num2))
else:
    print("El {} es mayor que el {}".format(num2,num1))

print("-------------------------- pedir una edad ------------------")

edad=int(input("Ingrese su edad"))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 anios")
else:
     print("No eres menor de edad")