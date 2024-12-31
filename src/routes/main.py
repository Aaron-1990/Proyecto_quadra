from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from ..models import Spot  # Agregamos la importación del modelo Spot

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Ruta principal que muestra la landing page si el usuario no está autenticado,
    o redirige al dashboard si lo está."""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('landing.html')

@main.route('/dashboard')
@login_required
def dashboard():
    """Muestra el dashboard del usuario con la lista de puestos y filtros.
    Requiere autenticación."""
    # Obtener todos los puestos
    spots = Spot.query.all()
    
    # Obtener tipos únicos de comida para el filtro
    # Usamos set para eliminar duplicados y sorted para ordenar alfabéticamente
    food_types = sorted(set(spot.food_type for spot in Spot.query.with_entities(Spot.food_type).distinct()))
    
    return render_template('dashboard.html', 
                         spots=spots,
                         food_types=food_types)