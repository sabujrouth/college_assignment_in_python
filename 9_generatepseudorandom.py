print("Sabuj Routh")
import random
import string

def generate_string(template):
    result = ""
    for char in template:
        if char == '_':
            result += random.choice(string.ascii_letters)
        else:
            result += char
    return result

template = "a____string"
print(generate_string(template))