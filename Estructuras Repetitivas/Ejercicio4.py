#Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

n=int (input ("Dime un numero del 1 al 5: "))
for i in range (1,11):
  print (i,"*",n,"=",i*n )




for n in range (1,6):
    print("la tabla del ", n)
    for i in range (1,11):
        print (n,"x",i,"=",i*n)




for n in range (1,11):
  print ("\n")
  print ("la tabla de multiplicar del",n,"es")
  print ("\n")
  for i in range (1,11):
    print (n,"x",i,"=",n*i)