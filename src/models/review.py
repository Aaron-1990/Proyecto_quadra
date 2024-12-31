from datetime import datetime
from .. import db
from .user import User

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Añadir la relación con User
    user = db.relationship('User', back_populates='reviews')

    def __repr__(self):
        return f'<Review {self.id} by User {self.user_id} for Spot {self.spot_id}>'