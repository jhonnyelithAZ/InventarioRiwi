#nombre del programa#

print("inventariado de productos")


#saludo al usuarrio#
print("Hola,bienvenido")

print("eligir una opcion valida")

#opciones del programa
while True:
    print("1.agregar producto")
    print("2.ver productos actuales")
    print("3.actualizar productos")
    print("4.eliminar productos")
    print("5.salir")
    
    opcion=int(input("ingrese una opcion: "))
    #en esta condicional,se estipula que si la opcion escogida no es ninguna de las indicadas,le dara un mensaje de invalides#
    if opcion not in (1,2,3,4,5):
        print("opcion invvalida")
        continue
    
    if opcion==1:
        #pedir el nombre,precio y cantidad de producto#
        nombre=input("ingrese el nombre del producto: ")
        precio=float(input("ingrese el precio del producto: "))
        cantidad=int(input("ingrese la cantidad de producto: "))   
    #imprimir el producto agregado#
        print(f"producto agregado: {nombre}// precio:{precio} // cantidad:{cantidad} // total:{precio*cantidad}")
    
    #en caso de que la opcion seleccionada sea 5,saldra un mensaje de adios#
    else:
        opcion==5
        print("good bye")
        break

#el programa en su etapa actual permite calcular el precio por la cantidad del producto agregado y mostrarlo en consola,tambien esta habilitado una opcion
#de no valido en caso de ingresar una opcion erronea y la opcion de salir#