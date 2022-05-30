#3.	Calcular el perímetro y área de un círculo dado su radio.
print ("Vamos a calcular el area y el perimetro de un circulo")
r =int (input ("Cuanto mide el radio "))
pi = float (3.14)
A = float (pi*r**2)
P = float (2*pi*r)
print ("El area es de ", A)
print ("El perimetro es de ", P)