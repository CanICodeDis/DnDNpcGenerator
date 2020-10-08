import platform
from pathlib import Path
import os
import codecs
import sys


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
                          'Kronmars Atem', 'Lindes Lohn', 'Sinvirs Flucht', 'Labanthers Mantel', 'Feuerschein', \
                          'Frosthöh')
        self.monat = 11
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
            print('Datei geöffnet: {}'.format(str(self.configpath + 'Kalenderconfig')))
        print('Kalender initialisiert')

    def incrementseconds(self, incsec):
        timetonextmin = 60 - self.sekunde
        while incsec >= 86400:  # ein Tag in Sekunden
            self.incrementdays(1)
            incsec -= 86400
        while incsec >= 3600:  # eine Stunde in Sekunden
            self.incrementhours(1)
            incsec -= 3600
        while incsec >= 60:  # eine Minute in Sekunden
            self.incrementminutes(1)
            incsec -= 60
        if incsec >= timetonextmin:
            self.incrementminutes(1)
            self.sekunde = incsec - timetonextmin
        else:
            self.sekunde += incsec

    def incrementminutes(self, incmin):
        timetonexthour = 60 - self.minute
        while incmin >= 44640:  # ein Monat in Minuten
            self.incrementmonths(1)
            incmin -= 44640
        while incmin >= 1440:  # ein Tag in Minuten
            self.incrementdays(1)
            incmin -= 1440
        while incmin >= 60:  # eine Stunde in Minuten
            self.incrementhours(1)
            incmin -= 60
        if incmin >= timetonexthour:
            self.incrementhours(1)
            self.minute = incmin - timetonexthour
        else:
            self.minute += incmin

    def incrementhours(self, inchours):
        timetonextday = 24 - self.stunde
        while inchours >= 8928:  # ein Jahr in Stunden
            self.incrementyears(1)
            inchours -= 8928
        while inchours >= 744:  # ein Monat in Stunden
            self.incrementmonths(1)
            inchours -= 744
        while inchours >= 24:
            self.incrementdays(1)
            inchours -= 24
        if inchours >= timetonextday:
            self.incrementdays(1)
            self.stunde = inchours - timetonextday
        else:
            self.stunde += inchours

    def incrementdays(self, incdays):
        timetonextmonth = 31 - self.monatstag
        while incdays >= 372:  # ein Jahr in Tagen
            self.incrementyears(1)
            incdays -= 372
        while incdays >= 31:
            self.incrementmonths(1)
            incdays -= 31
        if incdays > timetonextmonth:
            self.incrementmonths(1)
            self.monatstag = incdays - timetonextmonth
        else:
            self.monatstag += incdays

    def incrementmonths(self, incmonths):
        timetonextyear = 12 - self.monat
        while incmonths >= 12:
            self.incrementyears(1)
            incmonths -= 12
        if incmonths > timetonextyear:
            self.incrementyears(1)
            self.monat = incmonths - timetonextyear
        else:
            self.monat += incmonths

    def incrementyears(self, incyears):
        self.jahr += incyears

    def incrementcombatrounds(self, rounds):
        self.incrementseconds(6 * rounds)

    def telltime(self, output_channel=None):
        oldprint = sys.stdout
        if output_channel is not None:
            sys.stdout = output_channel
        print('{:02d}. {} {} - {:02d}:{:02d}:{:02d}'.format(self.monatstag, self.monatsref[self.monat - 1], self.jahr, \
                                                            self.stunde, self.minute, self.sekunde))
        if output_channel is not None:
            sys.stdout = oldprint

    def loadtime(self):
        with codecs.open(self.configpath + 'Kalenderconfig', 'r', encoding='utf8') as file:
            if os.path.getsize(self.configpath + 'Kalenderconfig') > 0:
                line = file.readline()
                datachunks = line.split(' - ')
                datum = datachunks[0].split(' ')
                zeit = datachunks[1].split(':')
                monthday = datum[0].split('.')
                print('Folgende Zeit geladen: ')
                print('Datum: {} {} {}'.format(datum[0], datum[1], datum[2]))
                print('Zeit: {}:{}:{}'.format(zeit[0], zeit[1], zeit[2]))
                self.monatstag = int(monthday[0])
                self.monat = self.monatsref.index(datum[1])
                print(self.monat)
                self.jahr = int(datum[2])
                self.stunde = int(zeit[0])
                self.minute = int(zeit[1])
                self.sekunde = int(zeit[2])
            else:
                print('Datei ist noch leer. Fahre mit den Standardeinstellungen fort:')
                self.telltime()

    def savetime(self):
        with codecs.open(self.configpath + 'Kalenderconfig', 'w', encoding='utf8') as file:
            self.telltime(output_channel=file)
            print('Folgende Zeit gespeichert: ')
            self.telltime()


time = fantasyTime()
time.incrementseconds(119)
time.incrementmonths(3)
time.incrementhours(9)
time.incrementminutes(59)
time.incrementcombatrounds(6)
time.savetime()
time.loadtime()
