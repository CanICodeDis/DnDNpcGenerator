from Kalender import fantasyTime as fTime
from pathlib import Path
import codecs
import sys
import os


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

    def register(self, time, zname, bname, dauerinsekunden):
        self. registriert = time
        self.ZustandsZauberName = zname
        self.ZustandsBesitzer = bname
        self.Savepath += self.ZustandsBesitzer + '__' + self.ZustandsZauberName
        self.isOn = True
        self.gesamtDauer = dauerinsekunden

    def getverblieben(self, jetzt):
        self.vergangeneDauer = jetzt - self.registriert
        self.verbliebeneDauer = self.gesamtDauer - self.vergangeneDauer
        if self.verbliebeneDauer < 0:
            self.isOn = False
            self.savezustand()
            return 0
        else:
            self.savezustand()
            return self.verbliebeneDauer

    def getvergangen(self, jetzt):
        self.vergangeneDauer = jetzt - self.registriert
        self.verbliebeneDauer = self.gesamtDauer - self.vergangeneDauer
        if self.verbliebeneDauer < 0:
            self.isOn = False
        self.savezustand()
        return self.vergangeneDauer

    def savezustand(self):
        if self.isOn:
            with codecs.open(self.Savepath, 'w', encoding='utf-8') as file:
                oldout = sys.stdout
                sys.stdout = file
                print("Gesamtdauer - {}".format(self.gesamtDauer))
                print("Vergangen - {}".format(self.vergangeneDauer))
                print("Verblieben - {}".format(self.verbliebeneDauer))
                print("Anfang - {}".format(self.registriert))
                print("Zustandsname - {}".format(self.ZustandsZauberName))
                print("Zustandsbesitzer - {}".format(self.ZustandsBesitzer))
                sys.stdout = oldout
        else:
            os.remove(self.Savepath)

