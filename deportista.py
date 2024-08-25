class Deportista:
    def __init__(self, deporte="Futbol", años_practicando=0):
        self.__deporte = deporte
        self.__años_practicando = años_practicando

    # Métodos get
    def getDeporte(self):
        return self.__deporte

    def getAñosPracticando(self):
        return self.__años_practicando

    # Métodos set
    def setDeporte(self, deporte):
        self.__deporte = deporte

    def setAñosPracticando(self, años_practicando):
        self.__años_practicando = años_practicando