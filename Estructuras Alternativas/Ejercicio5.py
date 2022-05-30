#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un  número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por  400.  
n=int (input ("Dime un año: "))
if n %4 !=0:
  print ("No es bisiesto")
elif n %4 ==0 and n %100 !=0:
  print ("Es bisiesto")
if n %100==0:
  print ("No es bisiesto")
if n%400 !=0:
  print ("No es bisiesto")
elif n %100 !=0 and n %400==0:
  print ("Es bisiesto")




año = int (input ("Dime un año: "))
print ("No es bisiesto" if año % 4 and (año % 100 or  not año % 400) else "es bisiesto")