from app import db

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(500), index=True, unique=True)
