from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    lista_futbolistas = []

    def __init__(self, nombre, edad, altura, sexo, años_practicando, goles_marcados, tarjetas_rojas, pierna_habil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", años_practicando)
        self.__goles_marcados = goles_marcados
        self.__tarjetas_rojas = tarjetas_rojas
        self.__pierna_habil = pierna_habil
        Futbolista.lista_futbolistas.append(self)

    # Métodos get
    def get_goles_marcados(self):
        return self.__goles_marcados

    def get_tarjetas_rojas(self):
        return self.__tarjetas_rojas

    def get_pierna_habil(self):
        return self.__pierna_habil

    # Métodos set
    def set_goles_marcados(self, goles_marcados):
        self.__goles_marcados = goles_marcados

    def set_tarjetas_rojas(self, tarjetas_rojas):
        self.__tarjetas_rojas = tarjetas_rojas

    def set_pierna_habil(self, pierna_habil):
        self.__pierna_habil = pierna_habil

    # Método str
    def __str__(self):
        return (f"Mi nombre es {self.get_nombre()}, soy profesional en el deporte {self.get_deporte()}. "
                f"Tengo {self.get_edad()} años de edad y llevo {self.get_años_practicando()} años en el deporte.")

