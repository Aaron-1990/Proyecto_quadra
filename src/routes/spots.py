from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from ..models import Spot, Review, Photo
from .. import db
from ..forms.spot import SpotForm
from flask import current_app
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import HiddenField

spots = Blueprint('spots', __name__)

class ReviewForm(FlaskForm):
    pass

@spots.route('/spots')
def index():
    """Lista todos los puestos de comida"""
    spots_list = Spot.query.all()
    return render_template('spots/index.html', spots=spots_list)

@spots.route('/spots/<int:id>')
def show(id):
    """Muestra los detalles de un puesto específico"""
    spot = Spot.query.get_or_404(id)
    reviews = Review.query.filter_by(spot_id=id).order_by(Review.created_at.desc()).all()
    form = ReviewForm()  # Crear instancia del formulario
    
    # Calcular promedio de calificaciones
    avg_rating = 0
    if reviews:
        avg_rating = sum(review.rating for review in reviews) / len(reviews)
    
    return render_template('spots/show.html', 
                         spot=spot, 
                         reviews=reviews, 
                         avg_rating=round(avg_rating, 1),
                         form=form)  # Pasar el formulario a la plantilla

@spots.route('/spots/<int:id>/review', methods=['POST'])
@login_required
def create_review(id):
    """Crear una nueva reseña para un puesto"""
    spot = Spot.query.get_or_404(id)
    
    # Verificar si el usuario ya ha hecho una reseña
    existing_review = Review.query.filter_by(user_id=current_user.id, spot_id=id).first()
    if existing_review:
        flash('Ya has realizado una reseña para este puesto.', 'warning')
        return redirect(url_for('spots.show', id=id))
    
    try:
        rating = int(request.form.get('rating'))
        if not 1 <= rating <= 5:
            raise ValueError('Rating debe estar entre 1 y 5')
            
        review = Review(
            user_id=current_user.id,
            spot_id=id,
            rating=rating,
            comment=request.form.get('comment')
        )
        
        db.session.add(review)
        db.session.commit()
        flash('Tu reseña ha sido publicada exitosamente.', 'success')
    except ValueError:
        flash('Error en la calificación. Debe ser un número entre 1 y 5.', 'error')
    except Exception as e:
        db.session.rollback()
        flash('Ocurrió un error al publicar tu reseña.', 'error')
    
    return redirect(url_for('spots.show', id=id))

@spots.route('/spots/new', methods=['GET', 'POST'])
@login_required
def create():
    """Crea un nuevo puesto de comida"""
    form = SpotForm()
    
    if form.validate_on_submit():
        try:
            # Convertir los objetos time a strings en formato "HH:MM"
            opening = form.opening_hours.data.strftime("%H:%M") if form.opening_hours.data else None
            closing = form.closing_hours.data.strftime("%H:%M") if form.closing_hours.data else None
            
            spot = Spot(
                name=form.name.data,
                description=form.description.data,
                location=form.location.data,
                latitude=form.latitude.data,
                longitude=form.longitude.data,
                food_type=form.food_type.data,
                opening_hours=opening,
                closing_hours=closing,
                owner=current_user
            )
            db.session.add(spot)
            db.session.commit()
            
            # Manejo de fotos si se subieron
            if form.photos.data:
                for photo in form.photos.data:
                    if photo and photo.filename:  # Verificar que haya un archivo
                        filename = secure_filename(photo.filename)
                        photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                        photo_obj = Photo(
                            spot_id=spot.id,
                            url=filename
                        )
                        db.session.add(photo_obj)
                db.session.commit()
                
            flash('Puesto creado exitosamente!')
            return redirect(url_for('spots.show', id=spot.id))
            
        except Exception as e:
            db.session.rollback()
            flash('Error al crear el puesto: ' + str(e), 'error')
            return render_template('spots/new.html', form=form)
            
    return render_template('spots/new.html', form=form)