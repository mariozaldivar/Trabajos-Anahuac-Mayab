import random

class Termometro():
    def __init__(self, tempC=random.randint(0, 100)):
        self.tempC = tempC

    def TemperaturaC(self):
        print(f"La temperatura en °C es: {self.tempC}°C ")
        return self.tempC
    
    def TemperaturaK(self):
        tempK = self.tempC + 273.15
        print(f"La temperatura en K es: {tempK}K ")
        return tempK
    
    def TemperaturaF(self):
        tempF = (self.tempC*9/5) + 32
        print(f"La temperatura en °F es: {tempF}°F ")
        return tempF
    
    def MostrarTemperatura(self):
        self.TemperaturaC()
        self.TemperaturaF()
        self.TemperaturaK()