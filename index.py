import sys
import random

welc = '''
Usage: index.py [case]

Cases:
  -v          Use vmess protocol
  -s          Use socketrocket protocol
  -h          Use http protocol
'''

class Reader:
    def __init__(self, filename, randomize=False):
        self.filename = filename
        with open(filename, 'r') as f:
            self.text = f.readlines()

        if randomize:
            random.shuffle(self.text)

    def __str__(self):
        return ''.join(self.text)

    def get_random_line(self):
        return random.choice(self.text)

def main(argc:int=len(sys.argv),argv:str=sys.argv) -> init:
    if argc == 1:
        print(welc)
