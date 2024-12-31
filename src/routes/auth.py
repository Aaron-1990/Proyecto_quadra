from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.urls import url_parse
from ..models import User
from .. import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            login_user(user, remember=remember)
            # Siempre redirigir al dashboard después de un login exitoso
            return redirect(url_for('main.dashboard'))
        flash('Por favor verifica tu email y contraseña')
    return render_template('auth/login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        # Obtener datos del formulario
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        accept_terms = request.form.get('accept_terms')

        # Validaciones
        if not accept_terms:
            flash('Debes aceptar los términos y condiciones')
            return redirect(url_for('auth.signup'))

        if password != password_confirm:
            flash('Las contraseñas no coinciden')
            return redirect(url_for('auth.signup'))

        if len(password) < 8:
            flash('La contraseña debe tener al menos 8 caracteres')
            return redirect(url_for('auth.signup'))

        if not any(c.isupper() for c in password):
            flash('La contraseña debe contener al menos una mayúscula')
            return redirect(url_for('auth.signup'))

        if not any(c.isdigit() for c in password):
            flash('La contraseña debe contener al menos un número')
            return redirect(url_for('auth.signup'))

        # Verificar si el usuario ya existe
        if User.query.filter_by(email=email).first():
            flash('El correo electrónico ya está registrado')
            return redirect(url_for('auth.signup'))
        
        if User.query.filter_by(username=username).first():
            flash('El nombre de usuario ya está en uso')
            return redirect(url_for('auth.signup'))

        # Crear nuevo usuario
        user = User(
            username=username,
            email=email,
            password=password
        )

        # Guardar en la base de datos
        db.session.add(user)
        try:
            db.session.commit()
            # Asegurarnos de que no haya sesión activa
            logout_user()  # Agregar esta línea
            flash('¡Cuenta creada exitosamente! Por favor inicia sesión.')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('Ocurrió un error al crear la cuenta. Por favor intenta de nuevo.')
            return redirect(url_for('auth.signup'))

    return render_template('auth/signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))