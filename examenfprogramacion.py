import csv 
import random
import math

sueldos = []

trabajadores = [
    {'nombre': 'Juan Perez', 'cargo': 'Consultor TI'},
    {'nombre': 'Maria Garcia', 'cargo': 'Analista'},
    {'nombre': 'Carlos Lopez', 'cargo': 'Programador'},
    {'nombre': 'Ana Martinez', 'cargo': 'Jefe de Proyecto'},
    {'nombre': 'Pedro Rodriguez', 'cargo': 'Consultor TI'},
    {'nombre': 'Laura Hernandez', 'cargo': 'Analista'},
    {'nombre': 'Miguel Sanchez', 'cargo': 'Programador'},
    {'nombre': 'Isabel Gomez', 'cargo': 'Jefe de Proyecto'},
    {'nombre': 'Francisco Diaz', 'cargo': 'Consultor TI'},
    {'nombre': 'Elena Fernandez', 'cargo': 'Analista'}
]

def asignar_sueldo():
    for trabajador in trabajadores:
        sueldo = random.randint(800000, 2000000)
        sueldos.append(sueldo)
    print(sueldos)

def clasificacion():
    print('Clasificación de sueldo')
    print('Sueldo bajo:')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo: ${sueldo}")
    print('Sueldo entre $800.000 y $2.000.000:')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo: ${sueldo}")
    print('Sueldo superior a $2.000.000:')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo: ${sueldo}")

def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
    print(f'Sueldo mas alto: {sueldo_max}')
    print(f'Sueldo mas bajo: {sueldo_min}')
    print(f'Promedio de sueldos: {sueldo_promedio}')
    print(f'Media geométrica de sueldo: {sueldo_geom}')

def reporte_sueldo():
        with open('info_trab.csv', 'w', newline='') as info_trab:
            escritor = csv.writer(info_trab)
            encabezado = ['Nombre Empleado', 'Cargo', 'Sueldo Base', 'Desc Salud', 'Desc AFP', 'Sueldo Bruto']
            escritor.writerow(encabezado)
            for trabajador, sueldo in zip(trabajadores, sueldos):
                salud = (sueldo * 7) / 100
                afp = (sueldo * 12) / 100
                sueldo_bruto = sueldo - salud - afp
                escritor.writerow([trabajador['nombre'], trabajador['cargo'], sueldo, int(salud), int(afp), int(sueldo_bruto)])
            print(f"Nombre:{trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo: ${sueldo}, Salud: {salud},AFP: {afp}, Sueldo Total: {sueldo_bruto}")
def salir_programa():
    print('Finalizar programa')
    print('Finalizando programa....')
    print('Desarrollado por Lucas Maulen')
    print('20.880.115-5')

def menu():
    while True:
        print('1. Asignar sueldo')
        print('2. Clasificar sueldos')
        print('3. Ver Estadísticas')
        print('4. Reporte de sueldos')
        print('5. Salir del programa')
        opc = int(input('Seleccione una opción: '))
        if opc == 1:
            asignar_sueldo()
        elif opc == 2:
            clasificacion()
        elif opc == 3:
            ver_estadisticas()
        elif opc == 4:
            reporte_sueldo()
        elif opc == 5:
            salir_programa()
            break
        else:
            print('Opción inválida')

if __name__ == "__main__":
    menu()