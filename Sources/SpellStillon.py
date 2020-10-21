from Kalender import fantasyTime as fTime
from pathlib import Path


class durationtracker:
    gesamtDauer = None
    vergangeneDauer = None
    verbliebeneDauer = None
    registriert = None
    ZustandsZauberName = None
    ZustandsBesitzer = None
    Savepath = None
    isOn = None

    def __init__(self):
        self.gesamtDauer = 0
        self.vergangeneDauer = 0
        self.verbliebeneDauer = 0
        self.registriert = 0
        self.ZustandsZauberName = ''
        self.ZustandsBesitzer = ''
        self.Savepath = Path.home() + '/DnD/Kampagne/WegNachVorn/Zustandsdauer/'

    def register(self, time, zname, bname):
        self. registriert = time
        self.ZustandsZauberName = zname
        self.ZustandsBesitzer = bname
        self.Savepath += self.ZustandsBesitzer
        self.isOn = True

    def setdauer(self, dauerinsekunden):
        self.gesamtDauer = dauerinsekunden

    def getverblieben(self, jetzt):
        self.vergangeneDauer = jetzt - self.registriert
        self.verbliebeneDauer = self.gesamtDauer - self.vergangeneDauer
        if self.verbliebeneDauer < 0:
            self.isOn = False
            return 0
        else:
            return self.verbliebeneDauer

    def getvergangen(self, jetzt):
        self.vergangeneDauer = jetzt - self.registriert
        self.verbliebeneDauer = self.gesamtDauer - self.vergangeneDauer
        if self.verbliebeneDauer < 0:
            self.isOn = False
        return self.vergangeneDauer

    def savezustand(self):
        pass


