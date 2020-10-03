from math import floor, ceil
from random import seed
from random import randint
from toolbox import read_random_object
from toolbox import generate_scores
from toolbox import pathbuilder
import platform
import png
import os
from pathlib import Path
from inventory import inventar


class NPC:
    name = None
    geburtstag = None
    geschlecht = None
    klasse = None
    volk = None
    persohnlichkeit = None
    portrait = None
    savepath = None
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

    def get_strmod(self):
        return self.strmod

    def get_dexmod(self):
        return self.dexmod

    def get_conmod(self):
        return self.conmod

    def get_intmod(self):
        return self.intmod

    def get_wismod(self):
        return self.wismod

    def get_chamod(self):
        return self.chamod

    def set_str(self, attr):
        self.str = int(attr)
        self.calculate_modifiers()

    def set_dex(self, attr):
        self.dex = int(attr)
        self.calculate_modifiers()

    def set_con(self, attr):
        self.con = int(attr)
        self.calculate_modifiers()

    def set_int(self, attr):
        self.int = int(attr)
        self.calculate_modifiers()

    def set_wis(self, attr):
        self.wis = int(attr)
        self.calculate_modifiers()

    def set_cha(self, attr):
        self.cha = int(attr)
        self.calculate_modifiers()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = str(name)

    def set_stufe(self, stufe):
        self.stufe = int(stufe)
        self.proficency = int(ceil(1.0 + 0.25 * self.stufe))

    def getstufe(self):
        return int(self.stufe)

    def get_portrait(self):
        return self.portrait

    def directorybuilder(self):
        ops = platform.system()
        pa = str(Path.home())
        if ops == 'Linux' or os == 'Darwin':
            pa = pa + '/DnD/NPCs/'
            pa = pa + str(self.volk) + '/' + str(self.klasse) + '/' + str(self.geschlecht) + '/\'' + str(self.name) + '\'/'
        else:
            pa = pa + '\\DnD\\NPCs\\'
            pa = pa + str(self.volk) + '\\' + str(self.klasse) + '\\' + str(self.geschlecht) + '\\\'' + str(self.name) + '\\\''
        if not os.path.exists(pa):
            os.makedirs(pa)
        self.savepath = pa

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

    def print_info(self):
        if self.name is not None:
            print('Name: ', self.name)
        if self.volk is not None:
            print('Volk: ', self.volk)
        if self.geschlecht is not None:
            print('Geschlecht: ', self.geschlecht)
        if self.persohnlichkeit is not None:
            print('Persöhnlichkeit: ', self.persohnlichkeit)
        if self.geburtstag is not None:
            print('Geburtstag: ', self.geburtstag)
        print('Klasse: ', self.klasse)
        print('Str: {} ({})'.format(str(self.str), str(self.strmod)))
        print('Dex: {} ({})'.format(str(self.dex), str(self.dexmod)))
        print('Con: {} ({})'.format(str(self.con), str(self.conmod)))
        print('Int: {} ({})'.format(str(self.int), str(self.intmod)))
        print('Wis: {} ({})'.format(str(self.wis), str(self.wismod)))
        print('Cha: {} ({})'.format(str(self.cha), str(self.chamod)))
        print('Stufe: {}'.format(str(self.stufe)))
        print('Proficency Bonus: {}'.format(str(self.proficency)))
        self.inv.printinventory()

    def __init__(self):
        seed(None)
        randomnum = randint(1, 2)
        if randomnum == 1:
            self.geschlecht = 'weiblich'
        else:
            self.geschlecht = 'männlich'
        opsys = platform.system()
        if opsys == 'Linux' or opsys == 'Darwin':
            self.persohnlichkeit = read_random_object('../Listen/CharEigenschaften')
            self.volk = read_random_object('../Listen/Volk')
            self.klasse = read_random_object('../Listen/Berufe')
        else:
            self.persohnlichkeit = read_random_object('..\\Listen\\CharEigenschaften')
            self.volk = read_random_object('..\\Listen\\Volk')
            self.klasse = read_random_object('..\\Listen\\Berufe')
        self.score_distributor()
        self.name = read_random_object(pathbuilder(self.geschlecht, self.volk))
        self.proficency = int(ceil(1.0 + 0.25 * self.stufe))
        self.inv = inventar()


x = NPC()
x.set_stufe(15)
x.print_info()
x.directorybuilder()
