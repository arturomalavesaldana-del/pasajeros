# Tarea U3 — Sistema de pasajeros con listas

Proyecto basado en `TAREA_U3_LISTAS_PASAJEROS.html`. Incluye dos implementaciones de listas, un menú de consola y los ocho ejercicios de la guía.

## Estructura

```text
TAREA_U3_LISTAS_PASAJEROS/
├── main.py
├── pasajero.py
├── lista_manual.py
├── lista_python.py
├── ejercicios.py
├── requirements.txt
└── tests/
    └── test_pasajeros.py
```

## Requisitos

- Python 3.10 o superior recomendado.
- No necesita instalar paquetes externos.

## Ejecutar

1. Descomprime el ZIP.
2. Abre la carpeta `TAREA_U3_LISTAS_PASAJEROS` en Visual Studio Code.
3. Abre una terminal en esa carpeta.
4. Ejecuta:

```bash
python main.py
```

En algunos equipos se utiliza `py main.py` o `python3 main.py`.

## Menú principal

1. Lista manual: arreglo fijo y movimientos implementados con ciclos.
2. Lista Python: métodos integrados de `list` y comprensiones.
3. Ejercicios: T1–T3 y P1–P5.
4. Salir.

Ambas listas ofrecen añadir, listar, insertar, búsqueda lineal, búsqueda binaria, modificar, eliminar por posición o cédula, ordenar ascendente/descendente, reversar, copiar, longitud, filtrar mayores de edad y convertir nombres a mayúsculas.

**Importante:** para que la búsqueda binaria funcione, ordena antes la lista por cédula en orden ascendente (opción 9).

## Ejecutar las pruebas

Desde la carpeta del proyecto:

```bash
python -m unittest discover -s tests -v
```
