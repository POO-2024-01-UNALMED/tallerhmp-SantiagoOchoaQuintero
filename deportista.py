class Deportista:
    def __init__(self, deporte="Futbol", años_practicando=0):
        self.__deporte = deporte
        self.__años_practicando = años_practicando

    # Métodos get
    def get_deporte(self):
        return self.__deporte

    def get_años_practicando(self):
        return self.__años_practicando

    # Métodos set
    def set_deporte(self, deporte):
        self.__deporte = deporte

    def set_años_practicando(self, años_practicando):
        self.__años_practicando = años_practicando