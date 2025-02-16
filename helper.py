import random
import string


def random_string_creation():
    random_char = ""
    for _ in range(10):
        random_char += random.choice(string.ascii_letters)
    return random_char


print((random_string_creation()))



