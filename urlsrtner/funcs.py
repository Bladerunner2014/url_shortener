import re
import string
from random import choice


def url_validator(url):
    regex = "^[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
    r = re.compile(regex)
    if re.search(r, url):
        return True
    else:
        return False


def short_url_generator(num):
    return ''.join(choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(num)) + '.ly'
