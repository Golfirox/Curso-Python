#Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un  número entero por teclado. A continuación va pidiendo números y va respondiendo si el  número a adivinar es mayor o menor que el introducido. El programa termina cuando se  acierta el número. 

n=int (input ("Dime un numero: "))
b=8
while True:
  if b<n:
    print ("El numero introducido es mayor ")
  elif b>n:
    print ("El numero introducido es menor ")
  elif n==b:
    print ("Acierto")
    break
  n = int (input ("Dime otro numero: "))
   