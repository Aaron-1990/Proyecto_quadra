from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, TimeField, FloatField, MultipleFileField
from wtforms.validators import DataRequired, Length, NumberRange

class SpotForm(FlaskForm):
    name = StringField('Nombre del puesto', validators=[DataRequired(), Length(min=3, max=80)])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    location = StringField('Ubicación', validators=[DataRequired()])
    latitude = FloatField('Latitud', validators=[DataRequired(), NumberRange(min=-90, max=90)])
    longitude = FloatField('Longitud', validators=[DataRequired(), NumberRange(min=-180, max=180)])
    food_type = SelectField('Tipo de comida', choices=[
        ('tacos', 'Tacos'),
        ('tortas', 'Tortas'),
        ('quesadillas', 'Quesadillas'),
        ('otros', 'Otros')
    ])
    opening_hours = TimeField('Hora de apertura', validators=[DataRequired()])
    closing_hours = TimeField('Hora de cierre', validators=[DataRequired()])
    photos = MultipleFileField('Fotos', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Solo se permiten imágenes.')
    ])