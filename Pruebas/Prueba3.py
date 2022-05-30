año = int (input ("Dime un año: "))
print ("Es bisiesto" if not año % 4 and (año % 100 or  not año % 400) 
  else: 
   print "No es bisiesto")