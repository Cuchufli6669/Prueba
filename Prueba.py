import csv

#Desde ya aviso que no está la verificación del rut

Dict_Estudiantes = {

}

Dict_Estudiantes_aprobados = {

}

Dict_Estudiantes_reprobados = {

}


def Registro_Estudiantes(nombre, rut, n1, n2, n3, n4, promedio, estado):

    Dict_Estudiantes[rut] = ("Nombre: ", nombre, "Nota: ", n1, n2, n3, n4, "Promedio: ", promedio, estado)

    if promedio >= 4:
        Dict_Estudiantes_aprobados[rut] = ("Nombre: ", nombre, "Notas: ", n1, n2, n3, n4, "Promedio: ", promedio, estado)
    else: 
        Dict_Estudiantes_reprobados[rut] = ("Nombre: ", nombre, "Notas: ", n1, n2, n3, n4, "Promedio: ", promedio, estado)


def Ver_estudiantes(Dict_Estudiantes):
    with open ("Estudiantes_registrados.csv", mode="w", newline="\n") as archivo_csv:
        agregar_csv = csv.writer(archivo_csv)
        agregar_csv.writerow(["Nombre, Rut, Notas, Promedio, Estado Academico del estudiante"])
        agregar_csv.writerow([Dict_Estudiantes])

    with open ("Estudiantes_registrados_aprobados.csv", mode="w", newline="\n") as archivo_csv:
        agregar_csv = csv.writer(archivo_csv)
        agregar_csv.writerow(["Nombre, Rut, Notas, Promedio, Estado Academico del estudiante"])
        agregar_csv.writerow([Dict_Estudiantes_aprobados])

    with open ("Estudiantes_registrados_reprobados.csv", mode="w", newline="\n") as archivo_csv:
        agregar_csv = csv.writer(archivo_csv)
        agregar_csv.writerow(["Nombre, Rut, Notas, Promedio, Estado Academico del estudiante"])
        agregar_csv.writerow([Dict_Estudiantes_reprobados])

    print("")
    print("")


    print(Dict_Estudiantes)


def Buscar_estudiantes(buscar_rut):
    if buscar_rut in Dict_Estudiantes:
        print(Dict_Estudiantes[buscar_rut])


while True: 
    print("1. Registro estudiantes")
    print("2. Ver estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    print("")
    print("")

    if opcion == "1":

        nombre = input("Ingrese el nombre del estudiante: ")

        try:
            rut = input("Ingrese el rut del estudiante (sin puntos pero con guión y dígito verificador): ")
            while len(rut) not in (7,8) and rut.isdigit():
                print("")
                print("Rut invalido, favor de ingresar uno que sea correcto")
                rut = input("Ingrese el rut del estudiante (sin puntos ni dígito verificador): ")
        except ValueError: 
            print("Favor de ingresar un rut válido")
        except: print("Hubo un error inesperado")


        try: 
            while True:
                n1 = float(input("Ingrese la nota 1 del estudiante: "))
                if n1 > 7 or n1 < 1:
                    print("Ingrese una nota correcta")
                else: 
                    break

            while True:
                n2 = float(input("Ingrese la nota 2 del estudiante: "))
                if n2 > 7 or n2 < 1:
                    print("Ingrese una nota correcta")
                else: 
                    break
            
            while True:
                n3 = float(input("Ingrese la nota 3 del estudiante: "))
                if n3 > 7 or n3 < 1:
                    print("Ingrese una nota correcta")
                else: 
                    break

            while True:
                n4 = float(input("Ingrese la nota 4 del estudiante: "))
                if n4 > 7 or n4 < 1:
                    print("Ingrese una nota correcta")
                else: 
                    break
            
            promedio = n1 * 0.3 + n2 * 0.3 * n3 * 0.3 + n4 * 0.1

            if promedio > 7:
                promedio = 7
            elif promedio < 1:
                promedio = 1

        except ValueError:
            print("Favor de colocar datos correctos")
        except:
            print("Lo sentimos, hubo una falla inesperada")

        estado = ""
        
        try:
            if promedio >= 4:
                estado = "Aprobado"
            else: estado = "Reprobado"
        except NameError:
            print("Hubo un error anteriormente, posiblemente al colocar las notas")
            print("Por favor ingresar las 4 notas correctamente")
        except: print("Hubo un error inesperado, intentelo de nuevo mas tarde")
    
        
        print("")
        print("")

        Registro_Estudiantes(nombre, rut, n1, n2, n3, n4, promedio, estado)

    elif opcion == "2":
        Ver_estudiantes(Dict_Estudiantes)
        print("")
        print("")

    elif opcion == "3":
        buscar_rut = input("Favor de ingresar el rut del estudiante: ")
        Buscar_estudiantes(buscar_rut)
        print("")
        print("")

    elif opcion == "4":
        break

    else: print("Seleccione una opcion válida")