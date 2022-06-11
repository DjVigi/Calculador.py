#Pedimos la operacion a realizar y los numeros a calcular
operacion = ("Dime la operacion a realizar")
x = int(input("Dime el primer numero))
y = int(input("Dime el segundo numero))
#Realizamos la condicion, segun que operacion le indiquemos ejecutara la operacion
if operacion == "Suma" or "suma":
  print("El resultado es =",x+y)
elif operacion == "Resta" or "resta":
  print("El resultado es =",x-y)
elif operacion == "Multiplicacion" or "multiplicacion":
  print("El resultado es =",x*y)
elif operacion == "Division or "division":
  print("El resultado es=",x/y)
