def lista_enlazada():
    #lista enlazada
    class Nodo(object):
        def __init__(self,datos,s=None):
            self.dato=datos
            self.siguientenodo=s
        def get_siguiente(self):
            return self.siguientenodo
        def set_siguiente(self,s):
            self.siguiente=s
        def get_datos(self):
            return self.dato
        def set_datos(self,datos):
            self.dato=datos
    class Lista_enlazada(object):
        def __init__(self,raiz=None):
            self.r=raiz
            self.tam=0
        def get_tamaño(self):
            return self.tam
        def agregar(self,datos):
            nodo_nuevo=Nodo(datos,self.r)
            self.r=nodo_nuevo
            self.tam+=1
        def eliminar(self,datos):
            ref_nodo=self.r
            nodo_anterior=None
            while ref_nodo:
                if ref_nodo.get_datos()==datos:
                    if nodo_anterior:
                        nodo_anterior.set_siguiente(ref_nodo.get_siguiente())
                    else:
                        self.r=ref_nodo.get_siguiente()
                        r=self.r
                    self.tam-=1
                    r=print("elemento eliminado")
                    return True
                else:
                    nodo_anterior=ref_nodo
                    ref_nodo=ref_nodo.get_siguiente()
            return False
        def buscarlista(self,datos):
            ref_nodo=self.r
            while ref_nodo:
                if ref_nodo.get_datos()==datos:
                    return datos
                else:
                    ref_nodo=ref_nodo.get_siguiente()
            return None


    menuprincipal = int(input("--Menú Principal: \n 1- Crear lista \n 2-Introducir elementos \n 3- eliminar elemento \n 4- recorrer lista \n 5-salir  \n Elija una opción: "))
    while menuprincipal!=5:
        #CREAR LISTA
        if menuprincipal==1:
            print("\n-----CREAR LISTA-----")
            nombre=(input("\nIntroduzca nombre de lista: "))
            lista = nombre
            lista=Lista_enlazada()
            print("\nLista: ",nombre,"creada con éxito")
            menuprincipal==input("\npreciones Enter para seguir: ")
        #INTRODUCIR
        elif menuprincipal==2:
            print("\n-------",nombre,"------")
            cantidad= int(input("Cuantos elementos desea introducir: "))
            for i in range(cantidad):
                 lista.agregar((input(str("Introduzca elemento: "))))
                
            print("se ha agregado a la lista! :)")
            menuprincipal==input("preciones Enter para seguir: ")
        #ELIMINAR
        elif menuprincipal==3:
            eliminar=(input("Introduzca elemento a borrar: "))
            lista.eliminar(eliminar)
            menuprincipal==input("preciones Enter para seguir: ")
        #BUSCAR EN LISTA
        elif menuprincipal==4:
            print("\n-----Buscar en",nombre,"------")
            print("Tamaño de lista: "+str(lista.get_tamaño()))
            buscarenlista=input("¿Cuál elemento desea acceder en lista?: ")
            print("\nElemento de lista: ",
                 lista.buscarlista(buscarenlista))
            
            if  lista.buscarlista(buscarenlista)== None:
                menuprincipal==input("preciones Enter para seguir: ")
            else:
                print("Desea realizar cambios en",buscarenlista,"?: ")
                menuseleccion=int(input("\n 1- Si \n 2- No \n Elija una opción: "))
                while menuseleccion!=2:
                    if menuseleccion==1:
                        print("\n-----MODIFICAR ELEMENTO DE ",nombre,"-----")
                        menu=int(input("\n 1-Cambiar nombre o valor de elemento \n 2- eliminar elemento \n 3- salir \n elija una opción: "))
                        while menu!=3:
                            if menu == 1:
                                e=lista.eliminar(buscarenlista)
                                print("tamaño de lista="+str(lista.get_tamaño()))
                                lista.agregar((input("Nuevo elemento :")))
                                print("¡elemento actualizado con éxito!")
                                print("tamaño="+str(lista.get_tamaño()))
                                menu==input("preciones Enter para seguir: ")
                            elif menu==2:
                                lista.eliminar(buscarenlista)
                                print("elemento eliminado con exito! ")
                                print("tamaño="+str(lista.get_tamaño()))
                                menu==input("preciones Enter para seguir: ")
                            else:
                                print("opción invalida")
                            break
                    else:
                        print("opción inválida")
                    break
        menuprincipal = int(input("\n\n--Menú Principal: \n 1- Crear lista \n 2-Introducir elementos \n 3- eliminar elemento \n 4- recorrer lista \n 5-salir  \n Elija una opción: "))
lista_enlazada()
