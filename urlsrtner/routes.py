from urlsrtner import app, db
from urlsrtner.models import Shortdb
from flask import request, redirect
from urlsrtner import funcs
# from flask_caching import Cache
#
# cache = Cache(config={'CACHE_TYPE': 'RedisCache', 'CACHE_REDIS_HOST': '0.0.0.0', 'CACHE_REDIS_PORT': 6379})


@app.get('/long/<string:long_url>')
def get_long_url(long_url):
    if funcs.url_validator(long_url):

        org_url = Shortdb(org_url=long_url, short_url=funcs.short_url_generator(5))
        db.session.add(org_url)
        db.session.commit()
        return org_url.short_url, 201
    else:
        return 'url is not valid'


@app.get('/short/<string:short_url>')
# @cache.cached(timeout=3600)
def redirect_to_org_link(short_url):
    link = Shortdb.query.filter_by(short_url=short_url).first()
    if link:
        link.counter += 1
        db.session.commit()

        return redirect(f"http://{link.org_url}", code=302)

    else:
        return 'short url is not valid'
