import json
import random
import string
from os import urandom

from requests import post

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (urandom(1024))

url = 'http://www.scammer.com'  # Scam URL

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(8))

    post(url, allow_redirects=False, data={
        'auid2yjauysd2uasdasdasd': username,  # Username Field Name + data element
        'kjauysd6sAJSDhyui2yasd': password  # Password Field Name + data element
    })

    print('sending username %s and password %s' % (username, password))

# regex convert to JSON array
# ^([A-Za-z]+)$
# "$1",