import codecs
from random import seed
from random import randint


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def read_line(fname, line):
    with codecs.open(fname, 'r', 'utf-8') as file:
        content = file.readlines()
        return content[line-1]


def read_random_object(fname):
    seed()
    with codecs.open(fname, 'r', 'utf-8') as file:
        for i, l in enumerate(file):
            pass
        randomnum = randint(0, i+1)
        file.seek(0)
        content = file.readlines()
        content[randomnum-1] = content[randomnum-1].replace('\r\n', '')
    return content[randomnum-1]


def generate_six_randoms():
    seed()
    array = []
    for i in range(6):
        array.append(randint(3, 18))
    return array
