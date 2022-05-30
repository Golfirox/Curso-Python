#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.  
a=int (input ("Dime un numetro entre el 1 y el 12 "))
if a==1:
  print ("Enero tiene 31 dias")
elif a==2:
  print ("Febrero tiene 28 dias")
elif a==3:
  print ("Marzo tiene 31 dias")
elif a==4:
  print ("Abril tiene 30 dias")
elif a==5:
  print ("Mayo tiene 31 dias")
elif a==6:
  print ("Junio tiene 30 dias")
elif a==7:
  print ("Julio tiene 31 dias")
elif a==8:
  print ("Agosto tiene 31 dias")
elif a==9:
  print ("Septiembre tiene 30 dias")
elif a==10:
  print ("Octubre tiene 31 dias")
elif a==11:
  print ("Noviembre tiene 30 dias")
elif a==12:
  print ("Diciembre tiene 31 dias")
else:
  print ("Mes no valido")