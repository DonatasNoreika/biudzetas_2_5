class Irasas:
    def __init__(self, suma, tipas):
        self.suma = suma
        self.tipas = tipas

    def __str__(self):
        return f"{self.tipas}: {self.suma}"
