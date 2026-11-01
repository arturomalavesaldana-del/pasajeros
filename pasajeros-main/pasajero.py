"""Modelo de datos para representar a un pasajero."""


class Pasajero:
    """Representa a una persona registrada como pasajero.

    Atributos:
        nombre (str): Nombre completo del pasajero.
        cedula (str): Número de cédula de 10 dígitos.
        edad (int): Edad del pasajero en años.
    """

    def __init__(self, nombre, cedula, edad):
        nombre = str(nombre).strip()
        cedula = str(cedula).strip()

        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if len(cedula) != 10 or not cedula.isdigit():
            raise ValueError("La cédula debe contener exactamente 10 dígitos.")
        if isinstance(edad, bool) or not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero mayor o igual a cero.")

        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def es_mayor_de_edad(self):
        """Devuelve True si el pasajero tiene 18 años o más."""
        return self.edad >= 18

    def __str__(self):
        """Devuelve una representación legible del pasajero."""
        return f"Nombre: {self.nombre} | Cédula: {self.cedula} | Edad: {self.edad}"

    def __repr__(self):
        return (
            f"Pasajero(nombre={self.nombre!r}, "
            f"cedula={self.cedula!r}, edad={self.edad!r})"
        )
