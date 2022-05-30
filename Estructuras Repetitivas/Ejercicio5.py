#Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
n = int(input("¿Qué número quieres saber si es primo? "))
contador = 0
for i in range (2,n):
  if n % i == 0:
    contador=contador+1
    print("divisor:", i)
 
if contador > 0 :
  print("El número no es primo" )
else:
  print("El nÚmero es primo")