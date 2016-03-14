from app import db

#######CATEGORY#######

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Category %r>' % (self.nickname)

#######EMAIL#######

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    entity = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Email %r>' % (self.email)

#######SUGGESTIONS#######

#TODO: ADD FIELDS
class S_Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    url = db.Column(db.String(128), index=True, unique=True)
    category = db.Column(db.Integer, db.ForeignKey('Category.id'))
    description = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return '<S_Event %r>' % (self.nickname)

#TODO: ADD FIELDS
class S_Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    url = db.Column(db.String(128), index=True, unique=True)
    category = db.Column(db.Integer, db.ForeignKey('Category.id'))
    description = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return '<S_Group %r>' % (self.nickname)


#######ENTITIES#######

#TODO: ADD properties
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    url = db.Column(db.String(128), index=True, unique=True)
    category = db.Column(db.String(32), index=True)
    description = db.Column(db.String(128), unique=True)
    timestamp = db.Column(db.DateTime)
    dateadded = db.Column(db.DateTime)
    Category = db.Column(db.Integer, db.ForeignKey('Category.id'))
    email = db.Column(db.Integer, db.ForeignKey('Email.id'))

    def __repr__(self):
        return '<Event %r>' % (self.nickname)

#TODO: ADD properties
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    url = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(128), unique=True)
    dateadded = db.Column(db.DateTime)
    category = db.Column(db.Integer, db.ForeignKey('Category.id'))

    def __repr__(self):
        return '<Group %r>' % (self.nickname)
