import random
import sys
import string



def RandomStringGenerator(l=12):
    randomer=string.ascii_letters+string.digits
    p=0
    s = ''
    while p<l:
        s += random.choice(randomer)
        p += 1
    return s

def BatchStringGenerator(n, min_len=8, max_len=12):
    r = []
    for i in range(n):
        length = None
        if min_len < max_len:
            import random
            length = random.choice(range(min_len, max_len))
        elif min_len == max_len:
            length = min_len
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(length))
    return r


min_len = input('Enter minimum string length: ')
max_len = input('Enter maximum string length: ')
n_strings = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n_strings), int(min_len), int(max_len)))
