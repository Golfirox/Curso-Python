#Pedir un número por teclado y mostrar la tabla de multiplicar (Con while y con for).
a =int (input ("Dime un numero "))
c = 0
while c < 11:
    print (a,"*",c,"=",a*c)
    c = c+1




#Pedir un número por teclado y mostrar la tabla de multiplicar (Con while y con for).
a =int (input ("Dime un numero "))
b =0
for b in range (11):
  print (a,"*",b,"=",a*b)