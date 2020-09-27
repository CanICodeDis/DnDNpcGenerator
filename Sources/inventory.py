import gegenstand

class inventar:

    Gegenstaende = []
    gesamtgewicht = 0

    def __init__(self):
        self.Gegenstaende = []
        self.gesamtgewicht = 0

    def hinzufuegen(self,name, anzahl, weight= None, description = None):
        self.Gegenstaende.append(gegenstand.Item(name, anzahl))
        if weight is not None:
            self.gesamtgewicht += weight