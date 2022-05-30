#Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa  o cero.
a = int (input ("Dime el 1er numero "))
b = int (input ("dime el 2º numero "))
c = int (a+b)
if c<0:
  print ("El valor es negativo")
elif c==0:
  print ("El valor es Cero")
elif c>0:
  print ("El valor es positivo")