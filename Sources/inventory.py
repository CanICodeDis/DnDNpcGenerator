from gegenstand import Item


class inventar:

    Gegenstaende = []
    gesamtgewicht = 0.0
    gesamtzahl = 0

    def __init__(self):
        self.Gegenstaende = []
        self.gesamtgewicht = 0.0
        self.gesamtzahl = 0

    def hinzufuegen(self, aname, anzahl, wert=None, weight=None, description=None):
        alreadyexists = 0
        for item in self.Gegenstaende:
            if item.get_name() == aname:
                item.set_count(item.get_count()+anzahl)
                self.gesamtzahl += anzahl
                self.gesamtgewicht += anzahl * item.get_gewicht()
                alreadyexists = 1
                break

        if anzahl > 0 and not alreadyexists:
            self.Gegenstaende.append(Item(aname, anzahl, wert, weight, description))
            self.gesamtzahl += anzahl
            if weight is not None:
                self.gesamtgewicht += anzahl * weight

    def entfernen(self, aname, anzahl):
        for item in self.Gegenstaende:
            if item.get_name() == aname:
                if item.get_count() > anzahl:
                    self.gesamtgewicht -= anzahl * item.get_gewicht()
                    self.gesamtzahl -= anzahl
                    item.set_count(item.get_count()-anzahl)
                elif item.get_count() == anzahl:
                    self.gesamtgewicht -= anzahl * item.get_gewicht()
                    self.gesamtzahl -= anzahl
                    self.Gegenstaende.remove(item)
                else:
                    cnt = item.get_count()
                    self. gesamtzahl -= cnt
                    self.gesamtgewicht -= cnt * item.get_gewicht()
                    self.Gegenstaende.remove(item)

    def printinventory(self):
        for item in self.Gegenstaende:
            item.print_item()
        print('Gesamtgewicht: {:.1f}'.format(self.gesamtgewicht))
        print('Anzahl aller Gegenstände: ', str(self.gesamtzahl))


# Inv = inventar()
# Inv.hinzufuegen('Buch', 3, '4 SP', weight=1.7, description='Ein leeres Buch')
# Inv.hinzufuegen('Buch', 3, '4 SP', description='Ein leeres Buch')
# Inv.hinzufuegen('Zauberstab', 1, '2 GP', weight=5.2, description='Ein krummer Zauberstab, riecht nach Obst')
# Inv.hinzufuegen('Eisenkugel', 247, '29CP', weight=0.02, description='Ein Haufen Eisenkugeln in einem Sack. Nützlich, um Dinge ins Rollen zu bringen!')
# Inv.entfernen('Buch', 3)
# Inv.printinventory()