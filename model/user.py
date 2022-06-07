from core.database import db


class User(db.Model):
    Host = db.Column(db.String(255), primary_key=True)
    User = db.Column(db.String(32), primary_key=True)
