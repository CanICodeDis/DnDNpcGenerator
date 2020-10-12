import codecs
from random import seed
from random import randint
import platform
from pathlib import Path


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
        randomnum = randint(0, i)
        file.seek(0)
        content = file.readlines()
        os = platform.system()
        if os == 'Linux' or os == 'Darwin':
            content[randomnum-1] = content[randomnum-1].replace('\n', '')
        else:
            content[randomnum - 1] = content[randomnum - 1].replace('\r\n', '')
    return content[randomnum-1]


def generate_scores():
    seed()
    array = []
    for i in range(6):
        array.append(randint(1, 6) + randint(1, 6) + randint(1, 6))
    return array


def pathbuilder(gesch, volk):
    os = platform.system()
    pa = str(Path.home())
    if os == 'Linux' or os == 'Darwin':
        path = pa + '/DnD/Listen/Namen/'
        path = path + str(gesch) + '/' + str(volk)
        # print(path)
    else:
        path = pa + '\\DnD\\Listen\\Namen\\'
        path = path + str(gesch) + '\\' + str(volk)
        # print(path)
    return path
