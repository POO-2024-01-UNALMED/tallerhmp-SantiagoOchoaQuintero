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
    def getGolesMarcados(self):
        return self.__goles_marcados

    def getTarjetasRojas(self):
        return self.__tarjetas_rojas

    def getPiernaHabil(self):
        return self.__pierna_habil

    # Métodos set
    def setGolesMarcados(self, goles_marcados):
        self.__goles_marcados = goles_marcados

    def setTarjetasRojas(self, tarjetas_rojas):
        self.__tarjetas_rojas = tarjetas_rojas

    def setPiernaHabil(self, pierna_habil):
        self.__pierna_habil = pierna_habil

    # Método str
    def __str__(self):
        return (f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} "
                f"Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte")

