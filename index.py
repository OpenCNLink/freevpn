import random

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
