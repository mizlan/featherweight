import random

def random_code(num_digits = 3):
    return ''.join(map(str, (random.randint(0, 9) for i in range(num_digits))))
