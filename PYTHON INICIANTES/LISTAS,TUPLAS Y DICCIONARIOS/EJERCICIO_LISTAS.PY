x =  input("ingrese su nombre: ")
y = input("ingrese su apellido: ")
nombre = []
apellido = []
nomyape = []
for i in range(len(x)):
    nombre.append(x[i])
    
for i in range(len(y)):
    apellido.append(y[i])
nomyape = nombre[:] + apellido [:] 
print("su nombre: " , nombre[:], "tiene: " , str(len(nombre)), " letras")
print("su apellido: " , apellido[:], "tiene: " , str(len(apellido)), " letras")
print("Su Nombre y apellido" ,nomyape[:],"tiene un total de : " , str(len(nomyape)), " letras")