from urlsrtner import app, db
from urlsrtner.models import Shortdb
from random import choice
import string
from flask import request, redirect


def short_url_generator(num):
    return ''.join(choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(num)) + '.ly'


@app.get('/long/<string:long_url>')
def get_long_url(long_url):
    # if Shortdb.query.filter_by(username=long_url).first():

    org_url = Shortdb(org_url=long_url, short_url=short_url_generator(5))
    db.session.add(org_url)
    db.session.commit()
    return org_url.short_url, 201


@app.get('/short/<string:short_url>')
def redirect_to_org_link(short_url):

    link = Shortdb.query.filter_by(short_url=short_url).first()
    if link:
        # link.counter++
        return redirect(f"http://{link.org_url}", code=302)

    else:
        return 'short url is not valid'




