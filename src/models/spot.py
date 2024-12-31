from datetime import datetime
from .. import db

class Spot(db.Model):
    __tablename__ = 'spots'
    
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    food_type = db.Column(db.String(50))
    opening_hours = db.Column(db.String(5))  # Cambiado a String para almacenar "HH:MM"
    closing_hours = db.Column(db.String(5))  # Cambiado a String para almacenar "HH:MM"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_verified = db.Column(db.Boolean, default=False)
    
    # Relaciones
    owner = db.relationship('User', backref='spots')
    photos = db.relationship('Photo', backref='spot', lazy=True)
    reviews = db.relationship('Review', backref='spot', lazy=True)