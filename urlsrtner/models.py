from urlsrtner import db
from datetime import datetime


class Shortdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    org_url = db.Column(db.String(500), unique=True, nullable=False)
    short_url = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.org_url}, {self.short_url} )"
