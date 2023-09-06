import random
import string

def generate_id(length: int = 4):
    return ''.join(random.choices(string.ascii_letters, k=length))
