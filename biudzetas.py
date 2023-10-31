import pickle
from irasas import Irasas

class Biudzetas:
    def __init__(self):
        self.zurnalas = self.gauti_zurnala()

    def gauti_zurnala(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
                return zurnalas
        except:
            zurnalas = []
            return zurnalas

    def irasyti_zurnala(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamas(self, suma):
        irasas = Irasas(suma, "pajamos")
        self.zurnalas.append(irasas)
        self.irasyti_zurnala()

    def prideti_islaidas(self, suma):
        irasas = Irasas(suma, "islaidos")
        self.zurnalas.append(irasas)
        self.irasyti_zurnala()

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "pajamos":
                suma += irasas.suma
            if irasas.tipas == "islaidos":
                suma -= irasas.suma
        return suma

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)