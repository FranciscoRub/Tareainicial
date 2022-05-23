
def cola():
    print("--------Cola--------")
    print("-----Lista de asistencia------")
    asist=[]
    def insertar(): 
        cantidad=(int(input("Introduzca cantidad de nombres a ingresar: ")))
        for i in range(cantidad):
            datos=input("\nNombre: ")
            asist.append(datos)
            print(asist)
    def eliminar():
        
        if len(asist):
           print("\nNombre extraido: ",asist.pop(0))
        else:
           print("\nLISTA VACÍA")
    def lista():
        for a in (asist):
            print(a)


    menuprincipal = int(input("--Menú Principal: \n 1- Insertar \n 2- Extraer \n 3- Visualizar \n 4- Salir  \n Elija una opción: "))
    while menuprincipal !=4:
        if menuprincipal == 1:
            insertar()
            print("\nSe añadió a",asist,"a la lista de asistencia")
            menuprincipal==input("preciones Enter para seguir: ")
        elif menuprincipal==2:
            eliminar()
            menuprincipal==input("preciones Enter para seguir: ")
        elif menuprincipal==3:
            print("\n--------LISTA-------")
            lista()
            menuprincipal==input("preciones Enter para seguir: ")
        else :
            print("digite un numero válido")
            menuprincipal==input("preciones Enter para volver a intentar: ")
        menuprincipal = int(input("\n\n--Menú Principal: \n 1- Insertar \n 2- Extraer \n 3- Visualizar \n 4- Salir  \n Elija una opción: "))

cola()
