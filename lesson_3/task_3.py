import random
import string
from itertools import zip_longest


def generate_dict(num_letters, num):
    letters = [x for x in ''.join(random.sample(string.ascii_lowercase, num_letters))]
    numbers = [random.randint(-100, 100) for _ in range(num)]
    if len(letters) > len(numbers):
        d = {x: y for x, y in zip_longest(letters, numbers)}
    else:
        d = {x: y for x, y in zip(letters, numbers)}
    return f'generated dict: {d}'


print(generate_dict(2, 4))
print(generate_dict(8, 5))


