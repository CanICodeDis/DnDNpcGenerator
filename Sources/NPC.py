from math import floor, ceil
from random import seed
from random import randint
from toolbox import read_random_object
from toolbox import generate_scores
from toolbox import pathbuilder
import platform
#import png
from class_cli import CLI
import os
from pathlib import Path
from inventory import inventar
import sys
import codecs

cli = CLI()


@cli.Program()
class NPC:
    name = None
    geburtstag = None
    geschlecht = None
    klasse = None
    volk = None
    persohnlichkeit = None
    portrait = None
    savepath = None
    invpa = None
    inv = None

    str = 0
    dex = 0
    con = 0
    int = 0
    wis = 0
    cha = 0

    strmod = 0
    dexmod = 0
    conmod = 0
    intmod = 0
    wismod = 0
    chamod = 0

    hp = 0
    ac = 0
    ini = 0

    stufe = 1
    proficency = 0

    res = None
    vul = None

    def calculate_modifiers(self):
        self.strmod = floor((self.str - 10.0) / 2.0)
        self.dexmod = floor((self.dex - 10.0) / 2.0)
        self.conmod = floor((self.con - 10.0) / 2.0)
        self.intmod = floor((self.int - 10.0) / 2.0)
        self.wismod = floor((self.wis - 10.0) / 2.0)
        self.chamod = floor((self.cha - 10.0) / 2.0)

    @cli.Operation()
    def get_strmod(self):
        return self.strmod

    @cli.Operation()
    def get_dexmod(self):
        return self.dexmod

    @cli.Operation()
    def get_conmod(self):
        return self.conmod

    @cli.Operation()
    def get_intmod(self):
        return self.intmod

    @cli.Operation()
    def get_wismod(self):
        return self.wismod

    @cli.Operation()
    def get_chamod(self):
        return self.chamod

    @cli.Setting()
    def set_str(self, attr):
        self.str = int(attr)
        self.calculate_modifiers()

    @cli.Operation()
    def set_dex(self, attr):
        self.dex = int(attr)
        self.calculate_modifiers()

    @cli.Operation()
    def set_con(self, attr):
        self.con = int(attr)
        self.calculate_modifiers()

    @cli.Operation()
    def set_int(self, attr):
        self.int = int(attr)
        self.calculate_modifiers()

    @cli.Operation()
    def set_wis(self, attr):
        self.wis = int(attr)
        self.calculate_modifiers()

    @cli.Operation()
    def set_cha(self, attr):
        self.cha = int(attr)
        self.calculate_modifiers()

    @cli.Operation()
    def get_name(self):
        return self.name

    @cli.Operation()
    def set_name(self, name):
        self.name = str(name)

    @cli.Operation()
    def set_stufe(self, stufe):
        self.stufe = int(stufe)
        self.proficency = int(ceil(1.0 + 0.25 * self.stufe))

    @cli.Operation()
    def getstufe(self):
        return int(self.stufe)

    @cli.Operation()
    def get_portrait(self):
        return self.portrait

    def directorybuilder(self):
        ops = platform.system()
        pa = str(Path.home())
        if ops == 'Linux' or ops == 'Darwin':
            pa = pa + '/DnD/Kampagne/WegNachVorn/NPCs/'
            pa = pa + str(self.volk) + '/' + str(self.klasse) + '/' + str(self.geschlecht) + '/\'' + str(self.name) + '\'/'
        else:
            pa = pa + '\\DnD\\Kampagne\\WegNachVorn\\NPCs\\'
            pa = pa + str(self.volk) + '\\' + str(self.klasse) + '\\' + str(self.geschlecht) + '\\\'' + str(self.name) + '\\\''
        if not os.path.exists(pa):
            os.makedirs(pa)
            if ops == 'Linux' or ops == 'Darwin':
                self.invpa = pa + 'Inventar/'
                os.makedirs(self.invpa)
            else:
                self.invpa = pa + 'Inventar\\'
                os.makedirs(self.invpa)
        self.savepath = pa
        self.inv.set_savepath(self.invpa)

    def score_distributor(self):
        if self.klasse is None:
            return
        else:
            numbers = generate_scores()
            numbers.sort(reverse=True)
            if self.klasse == 'Mönch':
                self.dex = numbers[0]
                self.wis = numbers[1]
                self.con = numbers[2]
                self.cha = numbers[3]
                self.int = numbers[4]
                self.str = numbers[5]
            elif self.klasse == 'Barbar':
                self.str = numbers[0]
                self.con = numbers[1]
                self.dex = numbers[2]
                self.cha = numbers[3]
                self.int = numbers[4]
                self.wis = numbers[5]
            elif self.klasse == 'Schurke':
                self.dex = numbers[0]
                self.int = numbers[1]
                self.con = numbers[2]
                self.wis = numbers[3]
                self.cha = numbers[4]
                self.str = numbers[5]
            elif self.klasse == 'Barde':
                self.cha = numbers[0]
                self.dex = numbers[1]
                self.int = numbers[2]
                self.con = numbers[3]
                self.wis = numbers[4]
                self.str = numbers[5]
            elif self.klasse == 'Paladin':
                self.str = numbers[0]
                self.cha = numbers[1]
                self.con = numbers[2]
                self.wis = numbers[3]
                self.dex = numbers[4]
                self.int = numbers[5]
            elif self.klasse == 'Hexer':
                self.cha = numbers[0]
                self.con = numbers[1]
                self.wis = numbers[2]
                self.dex = numbers[3]
                self.str = numbers[4]
                self.int = numbers[5]
            elif self.klasse == 'Magier':
                self.int = numbers[0]
                self.dex = numbers[1]
                self.con = numbers[2]
                self.wis = numbers[3]
                self.cha = numbers[4]
                self.str = numbers[5]
            elif self.klasse == 'Sorcerer':
                self.cha = numbers[0]
                self.con = numbers[1]
                self.wis = numbers[2]
                self.dex = numbers[3]
                self.str = numbers[4]
                self.int = numbers[5]
            elif self.klasse == 'Krieger':
                ismelee = randint(0, 1)
                if ismelee == 1:
                    self.str = numbers[0]
                    self.dex = numbers[1]
                else:
                    self.dex = numbers[0]
                    self.str = numbers[1]
                self.con = numbers[2]
                self.wis = numbers[3]
                self.cha = numbers[4]
                self.int = numbers[5]
            elif self.klasse == 'Druide':
                self.wis = numbers[0]
                self.con = numbers[1]
                self.int = numbers[2]
                self.dex = numbers[3]
                self.str = numbers[4]
                self.cha = numbers[5]
            elif self.klasse == 'Waldläufer':
                self.dex = numbers[0]
                self.wis = numbers[1]
                self.con = numbers[2]
                self.str = numbers[3]
                self.int = numbers[4]
                self.cha = numbers[5]
            elif self.klasse == 'Kleriker':
                self.wis = numbers[0]
                self.con = numbers[1]
                self.str = numbers[2]
                self.dex = numbers[3]
                self.cha = numbers[4]
                self.int = numbers[5]
            else:
                self.wis = 8
                self.con = 9
                self.str = 10
                self.dex = 11
                self.cha = 10
                self.int = 10
            self.calculate_modifiers()

    @cli.Operation()
    def print_info(self, outputchannel=None):
        oldout = None
        if outputchannel is not None:
            oldout = sys.stdout
            sys.stdout = outputchannel
        if self.name is not None:
            print('Name:', self.name)
        if self.volk is not None:
            print('Volk:', self.volk)
        if self.geschlecht is not None:
            print('Geschlecht:', self.geschlecht)
        if self.persohnlichkeit is not None:
            print('Persöhnlichkeit:', self.persohnlichkeit)
        if self.geburtstag is not None:
            print('Geburtstag:', self.geburtstag)
        print('Klasse:', self.klasse)
        print('Str: {} ({})'.format(str(self.str), str(self.strmod)))
        print('Dex: {} ({})'.format(str(self.dex), str(self.dexmod)))
        print('Con: {} ({})'.format(str(self.con), str(self.conmod)))
        print('Int: {} ({})'.format(str(self.int), str(self.intmod)))
        print('Wis: {} ({})'.format(str(self.wis), str(self.wismod)))
        print('Cha: {} ({})'.format(str(self.cha), str(self.chamod)))
        print('Stufe: {}'.format(str(self.stufe)))
        print('Proficency Bonus: {}'.format(str(self.proficency)))
        if outputchannel is not None:
            sys.stdout = oldout

    @cli.Operation()
    def savecharacter(self):
        with codecs.open(self.savepath + 'CharInfo', 'w',encoding='utf8') as file:
            self.print_info(outputchannel=file)

    @cli.Operation()
    def updateinventory(self):
        with codecs.open(self.invpa + 'InvInfo', 'w', encoding='utf8') as invfile:
            self.inv.printinventory(outputchannel=invfile)

    def specify(self, geschl=None, klasse=None, volk=None, name=None, persoenlichkeit=None):
        if geschl == 'm':
            self.geschlecht = 'männlich'
        elif geschl == 'w':
            self.geschlecht = 'weiblich'
        else:
            seed(None)
            rando = randint(1, 2)
            if rando == 1:
                self.geschlecht = 'weiblich'
            else:
                self.geschlecht = 'männlich'
        pa = str(Path.home())
        opsys = platform.system()
        if opsys == 'Linux' or opsys == 'Darwin':
            pa += '/DnD/Listen'
        else:
            pa += '\\DnD\\Listen'
        if klasse is None:
            if opsys == 'Linux' or opsys == 'Darwin':
                klasspath = pa + '/Berufe'
            else:
                klasspath = pa + '\\Berufe'
            self.klasse = read_random_object(klasspath)
        else:
            self.klasse = klasse
        self.score_distributor()
        if volk is None:
            if opsys == 'Linux' or opsys == 'Darwin':
                volkpath = pa + '/Volk'
            else:
                volkpath = pa + '\\Volk'
            self.volk = read_random_object(volkpath)
        else:
            self.volk = volk
        if name is None:
            self.name = read_random_object(pathbuilder(self.geschlecht, self.volk))
        else:
            self.name = name
        if persoenlichkeit is None:
            if opsys == 'Linux' or opsys == 'Darwin':
                perspath = pa + '/CharEigenschaften'
            else:
                perspath = pa + '\\CharEigenschaften'
            self.persohnlichkeit = read_random_object(perspath)
        else:
            self.persohnlichkeit = persoenlichkeit
        self.directorybuilder()

    @cli.Operation()
    def random_char(self):
        seed(None)
        randomnum = randint(1, 2)
        if randomnum == 1:
            self.geschlecht = 'weiblich'
        else:
            self.geschlecht = 'männlich'
        opsys = platform.system()
        pa = str(Path.home())
        if opsys == 'Linux' or opsys == 'Darwin':
            pa += '/DnD/Listen'
            self.persohnlichkeit = read_random_object(pa + '/CharEigenschaften')
            self.volk = read_random_object(pa + '/Volk')
            self.klasse = read_random_object(pa + '/Berufe')
        else:
            pa += '\\DnD\\Listen'
            self.persohnlichkeit = read_random_object(pa + '\\CharEigenschaften')
            self.volk = read_random_object(pa + '\\Volk')
            self.klasse = read_random_object(pa + '\\Berufe')
        self.score_distributor()
        self.name = read_random_object(pathbuilder(self.geschlecht, self.volk))
        self.proficency = int(ceil(1.0 + 0.25 * self.stufe))
        self.directorybuilder()

    def __init__(self):
        print('Neuer Charakter geboren')
        self.inv = inventar()


# x = NPC()
# x.specify(klasse='Barbar')
# x.set_stufe(15)
# x.directorybuilder()
# x.inv.hinzufuegen('Tekanne', 2, '10cp', 0.1, 'Eine schmucklose Teekanne aus Messing. Die Verarbeitung wirkt jedoch wertig.')
# x.print_info()
# x.savecharacter()
# x.updateinventory()
if __name__ == "__main__":
    NPC().CLI.main()
