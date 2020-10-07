import platform
from pathlib import Path
import os
import codecs


class fantasyTime:

    monatstag = None
    stunde = None
    minute = None
    sekunde = None
    wochentagsref = None
    wochentag = None
    monatsref = None
    monat = None
    jahr = None
    configpath = None
    configfile = None

    def __init__(self):
        self.monatstag = 1
        self.stunde = 0
        self.minute = 0
        self.sekunde = 1
        self.wochentagsref = ('Sonnentag', 'Felsentag', 'Windtag', 'Meerestag', 'Mondestag', 'Seelentag', 'Lebenstag')
        self.wochentag = 0
        self.monatsref = ('Gretstige', 'Mochtrath', 'Lyn', 'Ejnhar', 'Faarensted', 'Wassers Weg', \
                     'Kronmars Atem', 'Lindes Lohn', 'Labanthers Mantel')
        self.monat = 0
        self.jahr = 500
        self.configpath = str(Path.home())
        opsys = platform.system()
        if opsys == 'Linux' or opsys == 'Darwin':
            self.configpath = self.configpath + '/DnD/Kampagne/WegNachVorn/Kalender/'
        else:
            self.configpath += '\\DnD\\Kampagne\\WegNachVorn\\Kalender\\'
        if not os.path.exists(self.configpath):
            os.makedirs(self.configpath)
        with codecs.open(self.configpath + 'Kalenderconfig', 'w+') as self.configfile:
            print('Datei geöffnet: ', self.configfile)
        print('Kalender initialisiert')

    def savekalender(self):
        with codecs.open(self.configpath + 'Kalenderconfig', 'w') as self.configfile:
            self.configfile.write('Stunde: {}'.format(self.Stunde))
            self.configfile.write('Minute: {}'.format(self.minute))
            self.configfile.write('Sekunde: {}'.format(self.sekunde))
            self.configfile.write('Wochentag: {}'.format(self.wochentag))
            self.configfile.write('Datum: {}'.format(self.monatstag))
            self.configfile.write('Monat: {}'.format(self.monat))
            self.configfile.write('Jahr: {}'.format(self.jahr))
            print('Kalender überschrieben')

    def incrementseconds(self, incsec):
        timetonextmin = 60 - self.sekunde
        while incsec >= 60:
            self.incrementminutes(1)
            incsec -= 60
        if incsec >= timetonextmin:
            self.sekunde = incsec - timetonextmin
        else:
            self.sekunde += incsec
        print('Aktuelle Sekunden: {}'.format(self.sekunde))

    def incrementminutes(self, incmin):
        timetonexthour = 60 - self.minute
        while incmin >= 60:
            self.incrementhours(1)
            incmin -= 60
        if incmin >= timetonexthour:
            self.minute = incmin - timetonexthour
        else:
            self.minute += incmin
        print('Aktuelle Minuten: {}'.format(self.minute))

    def incrementhours(self, inchours):
        timetonextday = 24 - self.stunde
        while inchours >= 24:
            self.incrementdays(1)
            inchours -= 24
        if inchours >= timetonextday:
            self.stunde = inchours - timetonextday
        else:
            self.stunde += inchours
        print('Aktuelle Stunde: {}'.format(self.stunde))

    def incrementdays(self, incdays):
        timetonextmonth = 31 - self.monatstag
        while incdays >= 31:
            self.incrementmonths(1)
            incdays -= 31
        if incdays >= timetonextmonth:
            self.monatstag = incdays - timetonextmonth
        else:
            self.monatstag += incdays
        print('Aktueller Monatstag: {}'.format(self.monat))

    def incrementmonths(self, incmonths):
        timetonextyear = 12 - self.monat
        while incmonths >= 12:
            self.incrementyears(1)
            incmonths -= 12
        if incmonths >= timetonextyear:
            self.monatstag = incmonths - timetonextyear
        else:
            self.monatstag += incmonths
        print('Aktueller Monat: {}'.format(self.monat + 1))

    def incrementyears(self, incyears):
        self.jahr += incyears
        print('Aktuelles Jahr: {}'.format(self.jahr))


time = fantasyTime()
time.incrementseconds(120)