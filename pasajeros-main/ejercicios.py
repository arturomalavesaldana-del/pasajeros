"""Ocho ejercicios de la guía: tres desarrollados y cinco propuestos."""


def ejercicio_t1():
    from lista_python import ListaPasajerosPython
    from pasajero import Pasajero
    print("\nT1 — CRUD de pasajeros")
    lista = ListaPasajerosPython()
    for p in [Pasajero("Ana", "0912345678", 28), Pasajero("Luis", "0987654321", 35), Pasajero("Diana", "0923456789", 22)]:
        lista.añadir(p)
    lista.listar()
    print("Buscar Luis:", lista.buscar("0987654321"))
    lista.modificar("0987654321", "Luis Alberto", 36)
    lista.eliminar_por_valor("0923456789")
    lista.pasajeros.sort(key=lambda p: p.nombre)
    print("Después de modificar, eliminar y ordenar por nombre:")
    lista.listar()


def ejercicio_t2():
    print("\nT2 — Estadísticas de notas")
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]
    suma = 0
    mayor = menor = notas[0]
    indice_mejor = 0
    aprobados_manual = 0
    for i in range(len(notas)):
        suma += notas[i]
        if notas[i] > mayor:
            mayor, indice_mejor = notas[i], i
        if notas[i] < menor:
            menor = notas[i]
        if notas[i] >= 7:
            aprobados_manual += 1
    print(f"MANUAL: promedio {suma / len(notas):.2f} · Máx {mayor} ({nombres[indice_mejor]}) · Mín {menor} · Aprobados {aprobados_manual} de {len(notas)}")
    aprobados = [n for n in notas if n >= 7]
    print(f"PYTHON: promedio {sum(notas) / len(notas):.2f} · Máx {max(notas)} ({nombres[notas.index(max(notas))]}) · Mín {min(notas)} · Aprobados {len(aprobados)} de {len(notas)}")


def ejercicio_t3():
    print("\nT3 — Ordenamiento burbuja")
    original = [5, 2, 8, 1, 9, 3, 7]
    lista = original.copy()
    for fin in range(len(lista) - 1, 0, -1):
        hubo_swap = False
        for i in range(fin):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                hubo_swap = True
        if not hubo_swap:
            break
    print("MANUAL ascendente:", lista)
    print("PYTHON ascendente:", sorted(original))
    descendente = original.copy()
    descendente.sort(reverse=True)
    print("PYTHON descendente:", descendente)
    palabras = ["python", "a", "código", "el"]
    print("Palabras por longitud:", sorted(palabras, key=len))


def ejercicio_p1():
    print("\nP1 — Contar apariciones")
    lista, valor = [1, 3, 2, 3, 4, 3, 5], 3
    contador = 0
    for x in lista:
        if x == valor:
            contador += 1
    print("MANUAL:", valor, "aparece", contador, "veces")
    print("PYTHON count:", lista.count(valor))
    print("Comprensión:", len([x for x in lista if x == valor]))


def ejercicio_p2():
    print("\nP2 — Invertir sin reverse()")
    lista = [1, 2, 3, 4, 5]
    manual = []
    for i in range(len(lista) - 1, -1, -1):
        manual.append(lista[i])
    print("MANUAL:", manual)
    print("Slicing:", lista[::-1])
    print("reversed:", list(reversed(lista)))
    print("Comprensión:", [lista[i] for i in range(len(lista) - 1, -1, -1)])


def ejercicio_p3():
    print("\nP3 — Valores únicos manteniendo el orden")
    nums = [1, 3, 2, 3, 4, 1, 5, 2]
    unicos = []
    for x in nums:
        if x not in unicos:
            unicos.append(x)
    print("MANUAL:", unicos)
    print("dict.fromkeys:", list(dict.fromkeys(nums)))
    print("Nota: set no garantiza el orden de aparición.")


def ejercicio_p4():
    print("\nP4 — Segundo mayor distinto")
    nums = [5, 2, 9, 7, 9, 3, 8]
    mayor = segundo = None
    for x in nums:
        if mayor is None or x > mayor:
            if x != mayor:
                segundo = mayor
            mayor = x
        elif x != mayor and (segundo is None or x > segundo):
            segundo = x
    print(f"MANUAL: Mayor {mayor} · Segundo {segundo}")
    print("PYTHON:", sorted(set(nums))[-2:])


def ejercicio_p5():
    print("\nP5 — Fusionar listas ordenadas sin sort")
    a, b = [1, 3, 5, 7], [2, 4, 6, 8, 10]
    i = j = 0
    fusion = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            fusion.append(a[i]); i += 1
        else:
            fusion.append(b[j]); j += 1
    while i < len(a):
        fusion.append(a[i]); i += 1
    while j < len(b):
        fusion.append(b[j]); j += 1
    print("MANUAL:", fusion)
    print("PYTHON comprobación:", sorted(a + b))


EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas", "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)", "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor", "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista", "propuesto", ejercicio_p2),
    ("P3", "Números únicos", "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor", "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas", "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    while True:
        print("\n--- DESARROLLADOS (taller) ---")
        for codigo, titulo, tipo, _ in [e for e in EJERCICIOS if e[2] == "taller"]:
            print(f"{codigo}. {titulo}")
        print("--- PROPUESTOS ---")
        for codigo, titulo, tipo, _ in [e for e in EJERCICIOS if e[2] == "propuesto"]:
            print(f"{codigo}. {titulo}")
        print("0. Volver")
        codigo = input("Elige ejercicio: ").strip().upper()
        if codigo == "0":
            return
        encontrados = [e for e in EJERCICIOS if e[0] == codigo]
        if encontrados:
            encontrados[0][3]()
        else:
            print("Código no válido")
