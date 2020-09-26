from math import floor
from random import seed
from random import randint
from toolbox import read_random_object
from toolbox import generate_scores
from toolbox import pathbuilder
import platform


class NPC:
    name = None
    geburtstag = None
    geschlecht = None
    klasse = None
    volk = None
    persohnlichkeit = None
    portrait = None

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
    temphp = 0
    ac = 0
    ini = 0

    stufe = 1

    res = None
    vul = None

    def calculate_modifiers(self):
        self.strmod = floor((self.str - 10.0) / 2.0)
        self.dexmod = floor((self.dex - 10.0) / 2.0)
        self.conmod = floor((self.con - 10.0) / 2.0)
        self.intmod = floor((self.int - 10.0) / 2.0)
        self.wismod = floor((self.wis - 10.0) / 2.0)
        self.chamod = floor((self.cha - 10.0) / 2.0)

    def getname(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def setstufe(self, stufe):
        self.stufe = int(stufe)

    def getstufe(self):
        return int(self.stufe)

    def get_portrait(self):
        return self.portrait

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
                self.str = numbers[0]
                self.dex = numbers[1]
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
            self.calculate_modifiers()

    def print_info(self):
        print('Name: ', self.name)
        print('Volk: ', self.volk)
        print('Geschlecht: ', self.geschlecht)
        print('Persöhnlichkeit: ', self.persohnlichkeit)
        print('Klasse: ', self.klasse)
        print('Str: {} ({})'.format(str(self.str), str(self.strmod)))
        print('Dex: {} ({})'.format(str(self.dex), str(self.dexmod)))
        print('Con: {} ({})'.format(str(self.con), str(self.conmod)))
        print('Int: {} ({})'.format(str(self.int), str(self.intmod)))
        print('Wis: {} ({})'.format(str(self.wis), str(self.wismod)))
        print('Cha: {} ({})'.format(str(self.cha), str(self.chamod)))

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
            self.klasse = read_random_object('../Listen/Klassen')
        else:
            self.persohnlichkeit = read_random_object('..\\Listen\\CharEigenschaften')
            self.volk = read_random_object('..\\Listen\\Volk')
            self.klasse = read_random_object('..\\Listen\\Klassen')
        self.score_distributor()
        self.name = read_random_object(pathbuilder(self.geschlecht, self.volk))


x = NPC()
x.print_info()
