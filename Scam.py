import json
import random
import string
from os import urandom
from time import sleep

from requests import post


def randomInt(x, y):
    x = random.randint(x, y)
    return x


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (urandom(1024))

url = 'http://www.scammer.com'  # Scam URL

domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com', 'aol.com']

names = json.loads(open('names.json').read())
passwords = json.loads(open('passwords.json').read())

random.shuffle(names) # Randomize names list

for name in names:
    name_extra = ''.join(random.choice(string.digits))
    domain = ''.join(random.choice(domains))

    username = name.lower() + str(randomInt(1, 101)) + '@' + domain
    password = random.choice(passwords)

    post(url, allow_redirects=False, data={
        'auid2yjauysd2uasdasdasd': username,  # Username Field Name + data element
        'kjauysd6sAJSDhyui2yasd': password  # Password Field Name + data element
    })

    timer = randomInt(0, 7)
    print('waiting %s seconds...' % (timer))
    sleep(timer)

    print('sending username: %s and password: %s' % (username, password))



# regex convert to JSON array
# ^([A-Za-z]+)$
# "$1",