# from time import sleep
import string
from random import choice, randrange
# from

STRING = string.ascii_letters + string.digits + string.punctuation
char = []

count = 0

while count < 10:
    char.append(choice(STRING))
    count += 1
    
print(char)