import funciones as fn
import numpy as np

datosUsuario = []

print("Bienvenido")
arreglo = np.array(["99999999-RTX", "03034567-XXY", "12312345-CCU", "00000001-03F"])


while True:
    try:
        opcion = int(input("Selecione una de las siguientes opciones: \n1.Grabar \n2.Buscar \n3.Imprimir Certificados \n4.Salir \n"))
        if opcion == 4:
            print("Hasta luego")
            break
        elif opcion == 1:
            print("Ha seleccionado grabar")
            while True:
                try:
                    estado = False
                    nif = str(input("Ingrese su nif: ")).upper()

                    for i in range(len(arreglo)):

                        if arreglo[i] == nif:
                            estado = True
    
                    if estado == False:
                        print("El NIF ",nif," no se encuentra")
                    else:
                        print("El NIF ", nif," si se encuentra")
                        break
                except:
                    print("NIF incorrecto, ingrese nuevamente")
                #datosUsuario.append(nif)

            nombre = str(input("Ingrese su nombre y apellido: "))
            
            while True:
                try:
                    edad = int(input("Ingrese su edad: "))
                    if edad >= 0:
                        print("Edad ingresada correctamente")
                        break
                    else:
                        print("La edad debe ser mayor a 0")
                except:
                    print("Valor erróneo")
                #datosUsuario.append(edad)
            datosUsuario.append(nombre,nif,edad)
        elif opcion == 2:
            print("Ha elegido buscar")
            flag = False
            buscarNif = input("Ingrese el nif a buscar: ").upper()
            
            for f in range(len(datosUsuario)):
                if datosUsuario[f] == buscarNif:
                    flag = True
            if flag == False:
                print("El NIF ",buscarNif," no se encuentra")
            else:
                print("El NIF ",buscarNif," si se encuentra")
                print(datosUsuario)
                break
            
                
    

        elif opcion == 3:
            print("Ha seleccionado Imprimir Certificados")



            

            

            

                        

                    


    except:
        print("Valor fuera de rango")