#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido  “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.  
n = str (input ("Dime tu nombre: "))
if n=="pepe":
  print ("Usuario correcto")
  p = str (input ("Contraseña: "))
  if p=="asdasd":
    print ("Contraseña Correcta ")
  else:
    print ("Contraseña incorrecta")
else:
  print ("usuario incorrecto")