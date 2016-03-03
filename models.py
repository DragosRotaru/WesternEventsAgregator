from app import db

class S_Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    url = db.Column(db.String(128), index=True, unique=True)
    category = db.Column(db.String(32), index=True)
    description = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return '<S_Link %r>' % (self.nickname)
