"""Programa principal del proyecto Tarea U3 - Listas de pasajeros."""
from pasajero import Pasajero
from lista_manual import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from ejercicios import menu_ejercicios

lista1 = ListaPasajerosManual(capacidad=10)
lista2 = ListaPasajerosPython()


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")


def leer_pasajero():
    nombre = input("Nombre: ").strip()
    cedula = input("Cédula (10 dígitos): ").strip()
    edad = leer_entero("Edad: ")
    if not nombre or len(cedula) != 10 or not cedula.isdigit() or edad < 0:
        print("Datos no válidos. Verifique nombre, cédula de 10 dígitos y edad.")
        return None
    return Pasajero(nombre, cedula, edad)


def cargar_datos_prueba(lista):
    datos = [("Diana", "0923456789", 22), ("Ana", "0912345678", 28), ("Luis", "0987654321", 35), ("Beto", "0934567890", 16), ("Elena", "0901234567", 41)]
    cargados = 0
    for nombre, cedula, edad in datos:
        if lista.añadir(Pasajero(nombre, cedula, edad)):
            cargados += 1
    print(f"Se añadieron {cargados} pasajeros de prueba.")


def mostrar_menu_lista(titulo):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir pasajero (al final)\n 2. Listar pasajeros\n 3. Insertar en una posición\n 4. Buscar por cédula (lineal)\n 5. Buscar por cédula (binaria; ordenar antes)\n 6. Modificar pasajero\n 7. Eliminar por posición\n 8. Eliminar por cédula\n 9. Ordenar ascendente por cédula\n10. Ordenar descendente por cédula\n11. Reversar\n12. Copiar lista\n13. Longitud\n14. Filtrar mayores de edad\n15. Nombres en mayúsculas\n C. Cargar datos de prueba\n 0. Volver")


def ejecutar_menu(lista, titulo, es_manual=False):
    while True:
        mostrar_menu_lista(titulo)
        op = input("Opción: ").strip().upper()
        if op == "1":
            p = leer_pasajero()
            if p and lista.añadir(p): print("✓ Pasajero añadido")
        elif op == "2":
            lista.listar()
        elif op == "3":
            pos = leer_entero("Posición: "); p = leer_pasajero()
            if p and lista.insertar(pos, p): print("✓ Pasajero insertado")
        elif op in ("4", "5"):
            cedula = input("Cédula a buscar: ").strip()
            if op == "5":
                print("Aviso: la lista debe estar ordenada ascendentemente por cédula.")
            pos = lista.buscar(cedula) if op == "4" else lista.buscar_binaria(cedula)
            if pos == -1: print("No se encontró el pasajero.")
            else:
                pasajero = lista.datos[pos] if es_manual else lista.pasajeros[pos]
                print(f"Encontrado en [{pos}]: {pasajero}")
        elif op == "6":
            cedula = input("Cédula del pasajero: ").strip()
            nombre = input("Nuevo nombre: ").strip()
            edad = leer_entero("Nueva edad: ")
            if lista.modificar(cedula, nombre, edad): print("✓ Pasajero modificado")
        elif op == "7":
            eliminado = lista.eliminar_por_posicion(leer_entero("Posición a eliminar: "))
            if eliminado: print("✓ Eliminado:", eliminado)
        elif op == "8":
            if lista.eliminar_por_valor(input("Cédula a eliminar: ").strip()): print("✓ Pasajero eliminado")
            else: print("No se encontró la cédula.")
        elif op == "9":
            lista.ordenar_asc(); lista.listar()
        elif op == "10":
            lista.ordenar_desc(); lista.listar()
        elif op == "11":
            lista.reversar(); lista.listar()
        elif op == "12":
            copia = lista.copiar(); copia.reversar()
            print("--- COPIA (reversada) ---"); copia.listar()
            print("--- ORIGINAL (sin cambios de orden) ---"); lista.listar()
        elif op == "13":
            print(f"Hay {lista.longitud()} pasajeros")
        elif op == "14":
            print("--- Pasajeros mayores de edad ---"); lista.filtrar_mayores_de_edad().listar()
        elif op == "15":
            print(lista.nombres_en_mayusculas())
        elif op == "C":
            cargar_datos_prueba(lista)
        elif op == "0":
            return
        else:
            print("Opción no válida")


def menu_lista1():
    ejecutar_menu(lista1, "LISTA 1 · construida desde cero", True)


def menu_lista2():
    ejecutar_menu(lista2, "LISTA 2 · list de Python", False)


def main():
    while True:
        print("\n╔══════════════════════════════════╗\n║   TAREA LISTAS · PASAJEROS ✈     ║\n╚══════════════════════════════════╝")
        print("1. Lista 1 (construida desde cero)\n2. Lista 2 (list de Python)\n3. Listar ejercicios\n4. Salir")
        op = input("Opción: ").strip()
        if op == "1": menu_lista1()
        elif op == "2": menu_lista2()
        elif op == "3": menu_ejercicios()
        elif op == "4":
            print("¡Hasta pronto!"); break
        else: print("Opción no válida")


if __name__ == "__main__":
    main()