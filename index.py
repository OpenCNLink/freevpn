import os
import sys
import random
import base64

USAGE = """
Usage: index.py [case]

Cases:
  -v, --vmess         Use vmess protocol
  -s, --socketrocket  Use socketrocket protocol
  -h, --http          Use http protocol
"""

class Reader:
    def __init__(self, filename, randomize=False):
        with open(filename, 'r') as f:
            self.text = f.readlines()
        
        if randomize:
            random.shuffle(self.text)

    def __str__(self):
        return ''.join(self.text)

    def get_random_line(self):
        return random.choice(self.text)

def main(args=sys.argv[1:]) -> None:
    if not args:
        print(USAGE.strip())
        return

    case = args[0]
    if case in ('-v', '--vmess'):
        proxy = Reader('./list/vmess.txt')
        print(base64.b64encode(str(proxy).encode()).decode())
    elif case in ('-s', '--socketrocket'):
        proxy = Reader('./list/socketrocket.txt')
        print(proxy)
    elif case in ('-h', '--http'):
        os.system('python ./http/init.py')
    else:
        print('Invalid option.')

if __name__ == '__main__':
    sys.exit(main())