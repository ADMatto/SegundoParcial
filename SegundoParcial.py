import csv
import os

# a)Tener un menú de acciones
def menu():
    while True:
        print("Opciones: \n    1) Cargar Datos\n    2) Vacaciones\n'Salir' para salir")
        opcion = input("Ingrese la opcion: ")
        if opcion == '1':
            cargar_Datos()
        if opcion == '2':
            vacaciones()
        if opcion.upper() == 'SALIR':
            return
        else:
            print('La opcion ingresada no es correcta!')


'''b) Permitir la carga de datos y guardarlos en un archivo csv cuyo nombre será dado por el usuario. 
Si el archivo ya existe deberá preguntar si se desea modificar o sobreescribirlo. * sólo validar que 
legajo y total de vacaciones sean números enteros.'''
def cargar_Datos():
    campos = ['Legajo', 'Nombre', 'Apellido', 'Total Vacaciones']
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
        print(legajo)
        lista_temporal.append(legajo)
        print(lista_temporal)
        seguir_ingresando = input("Ingrese 'S' si desea seguir ingresando datos: ")
    nombre_archivo = input('Ingrese el nombre del archivo a guardar: ')
    guardar_informacion(nombre_archivo, lista_temporal)
        sobrescribir = input('El archivo ya existe, desea sobrescribirlo? s/n: ')
        Print('I')

def guardar_informacion(nombre, lista_de_datos):
    if os.path.isfile(nombre) == True:
        print('El archivo ya existe! Desea sobrescribirlo? s/n: ')


'''c) Dado el número de legajo de un empleado calcular e informar en pantalla los días que le quedan disponibles de 
vacaciones junto con el resto de sus datos. Por ejemplo "Legajo 1 : Laura Estebanez, le restan 11 días de vacaciones"'''
def vacaciones():
    pass


def main():
    menu()




main()
