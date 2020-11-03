import csv
import os

campos = ['Legajo', 'Nombre', 'Apellido', 'Total Vacaciones']
# a)Tener un menú de acciones
def menu():
    nombre_archivo = ''
    while True:
        print("Opciones: \n    1) Cargar Datos\n    2) Vacaciones\n'Salir' para salir")
        opcion = input("Ingrese la opcion: ")
        if opcion == '1':
            nombre_archivo = cargar_Datos()
        if opcion == '2':
            if nombre_archivo == '':
                print("No existen registros recientes de empleados!")
            else:
                vacaciones(nombre_archivo)
        if opcion.upper() == 'SALIR':
            return


'''b) Permitir la carga de datos y guardarlos en un archivo csv cuyo nombre será dado por el usuario. 
Si el archivo ya existe deberá preguntar si se desea modificar o sobreescribirlo. * sólo validar que 
legajo y total de vacaciones sean números enteros.'''
def cargar_Datos():
    legajo = {}
    lista_temporal = []
    seguir_ingresando = 'S'
    while seguir_ingresando.upper() == 'S':
        for campo in campos:
            if campo == 'Legajo' or campo == 'Total Vacaciones':
                while True:
                    try:
                        numero = int(input(f'Ingrese {campo}: '))
                        break
                    except ValueError:
                        print('Debe ser un numero entero!')
                legajo[campo] = numero
            else:
                legajo[campo] = input(f'Ingrese {campo}: ')
        lista_temporal.append(legajo.copy())
        seguir_ingresando = input("Ingrese 'S' si desea seguir ingresando datos: ")
    # validar nombre_archivo
    nombre_archivo = input('Ingrese el nombre del archivo a guardar: ')+'.csv'
    guardar_informacion(nombre_archivo, lista_temporal)
    return nombre_archivo


def guardar_informacion(nombre, lista_de_datos):
    abrir = "w"
    if os.path.isfile(nombre):
        while True:
            sobrescribir = input('El archivo ya existe! Ingrese "m" para modificarlo o "s" para sobrescribir: ')
            if sobrescribir.upper() == 'M':
                abrir = "a"
                break
            if sobrescribir.upper() == 'S':
                break
            else:
                print('La opcion ingresada no es correcta!')
    try:
        with open(nombre, abrir, newline='') as f:
            writer = csv.DictWriter(f, delimiter=';', fieldnames=campos)
            if abrir.upper() == 'W':
                writer.writeheader()
            for legajo in lista_de_datos:
                writer.writerow(legajo)
            print(f'Archivo {nombre} guardado!')
    except IOError:
        print('Error al abrir el archivo!')


'''c) Dado el número de legajo de un empleado calcular e informar en pantalla los días que le quedan disponibles de 
vacaciones junto con el resto de sus datos. Por ejemplo "Legajo 1 : Laura Estebanez, le restan 11 días de vacaciones"'''
def vacaciones(nombre_archivo):
    cant_dias = 0
    while True:
        try:
            nro_legajo = int(input('Ingrese numero de legajo: '))
            break
        except ValueError:
            print('El valor ingresado no es un numero valido!')
    try:
        with open("dias.csv", "r", newline='') as dias:
            reader = csv.DictReader(dias, fieldnames=['Legajo', 'Fecha'])
            for fila in reader:
                if fila['Legajo'] == f'{nro_legajo}':
                    cant_dias += 1
    except IOError or UnboundLocalError:
        print("Error al abrir el archivo de vacaciones!")
    try:
        with open(nombre_archivo, "r", newline='') as empleados:
            reader = csv.reader(empleados, delimiter=";")
            for datos in reader:
                if datos[0] == str(nro_legajo):
                    print(f'Legajo {nro_legajo} : {datos[1]} {datos[2]} le restan {int(datos[3])-cant_dias} días de vacaciones')
    except IOError:
        print("Error al abrir el archivo!")


menu()
