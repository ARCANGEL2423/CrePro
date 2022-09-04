#Mendoza Romero Angel Emiliano 5IM10

pasos=[]


print("¡HOLA! \n")
print("Crea tu propio protocolo")

def menu():
     print("")
     print("_--_;;;_=_ Menú _=_;;;_--_ \n")
     print("Elije una opción: \n")
     print("1. Agregar un paso en una posición especifica")
     print("2. Poner un paso")  
     print("3. Borrar un paso")
     print("4. Cambiar un paso")
     print("5. Mostrar el protocolo")
     print("6. Salir \n")
     print("Tenga en cuenta que el paso 1 le pertenece la posición 0 \n")



long = int(input("¿Cuántos pasos deseas agregar?  (el paso 1 le pertenece la posición 0): "))
i=0

while i < long:
    step = input("Agrega el paso "+str(i+1)+" : ")

    pasos.append(step)

    i = i + 1


while True:
    menu()
    opc=int(input("Escoge una opción: "))
    
    if opc == 1:
        i=0
        loc=int(input("Escribe la posición en la que desea añadir el paso: "))
        no=input("Escribe el nuevo paso: ")
        print("")
        pasos.insert(loc,no)
        for m in range (0,(len(pasos))):
            print("Paso " +str(i+1)+" : "+pasos[i])
            i = i + 1
            print("")
            
    elif opc == 2:
         i=0
         add=input("Escribe el nuevo paso: ")
         pasos.append(add)
         print("")
         for p in range (0,(len(pasos))):
             print("Paso " +str(i+1)+" : "+pasos[i])
             i = i + 1
             print("")

    elif opc == 3:
        i=0
        dele = int(input("Da la posición del paso a eliminar: "))
        print("")
        pasos.pop(dele)
        for n in range (0,(len(pasos))):
            print("Paso " +str(i+1)+" : "+pasos[i])
            i = i + 1
            print("")
                     

    elif opc == 4:
         i=0
         mod = int(input("Escribe la posición del paso que deseas cambiar: "))
         pasos.pop(mod)
         new = input("Escribe el paso modificado: ")
         print("")
         pasos.insert(mod,new)
         for y in range (0,(len(pasos))):
            print("Paso " +str(i+1)+" : "+pasos[i])
            i = i + 1
            print("")

    elif opc == 5:
         i=0
         print("Aquí está tu protocolo:")
         print("")
         for j in range (0,(len(pasos))):
                print("Paso " +str(i+1)+" : "+pasos[i])
                i = i + 1
                print("")
            
    elif opc == 6:
          print("")
          print("¡HASTA LA PROXIMA!")

          break
    else:
          print("")
          print("Opción inválida, intentalo de nuevo. \n")
