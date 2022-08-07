

class Item:

    name = None
    weight = 0.0
    count = 0
    description = None
    wert = None

    def __init__(self):
        self.name = 'Kein Name festegelgt'
        self.weight = 0.0
        self.count = 0
        self.wert = 'Kein Wert festgelegt.'
        self.description = 'Keine Beschreibung hinterlegt.'

    def __init__(self, name, count, wert, weight, despript=None):
        self.name = str(name)
        self.count = int(count)
        self.wert = str(wert)
        self.weight = float(weight)
        if despript is not None:
            self.description = str(despript)
        else:
            self.description = 'Keine Beschreibung hinterlegt.'

    def set_name(self, sname):
        self.name = str(sname)

    def set_weigth(self, iweigth):
        self.weight = float(iweigth)

    def set_wert(self, iwert):
        self.wert = str(iwert)

    def set_beschreibung(self, sdesc):
        self.description = str(sdesc)

    def set_count(self, icount):
        self.count = icount

    def get_name(self):
        return str(self.name)

    def get_wert(self):
        return str(self.wert)

    def get_gewicht(self):
        return float(self.weight)

    def get_description(self):
        return str(self.description)

    def get_count(self):
        return int(self.count)

    def print_item(self):
        print('Name: ', self.name)
        print('Anzahl: ', self.count)
        print('Gewicht pro Einheit: {:.2f}'.format(self.weight))
        print('Wert: ', str(self.get_wert()))
        print('Beschreibung:', str(self.get_description()))
