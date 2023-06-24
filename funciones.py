import numpy as np

arreglo = np.array(["99999999-RTX", "03034567-XXY", "12312345-CCU", "00000001-03F"])


'''def buscarNif(nif):
    nif = input("Ingrese su nif: ")
    estado == False
    for i in range(len(arreglo)):

        if arreglo[i] == nif:
            estado = True
    
        if estado == False:
            print("El NIF ",nif," no se encuentra")
        else:
            print("El NIF ", nif," si se encuentra")
            break
    return'''
'''datosUsuario = ["99999999-RTX","Julio Cifuentes",29]
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
        break'''