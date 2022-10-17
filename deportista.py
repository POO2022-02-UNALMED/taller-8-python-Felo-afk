class Deportista():
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, d):
        self._deporte = d

    def getAñosPracticando(self):
        return self._añosPracticando

    def setAñosPracticando(self, a):
        self._añosPracticando = a
