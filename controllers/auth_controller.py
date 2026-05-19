from flask import Blueprint, request, redirect, url_for, session, render_template
from models.usuario_model import Usuario
import views.auth_view as auth_view

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario.get_by_email(email)
        if usuario and usuario.verify_password(password):
            session['user_id'] = usuario.id
            session['user_nombre'] = usuario.nombre
            return redirect(url_for('medico.index'))
        else:
            return auth_view.login(error='Credenciales inválidas')
    return auth_view.login()

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        if Usuario.get_by_email(email):
            return auth_view.registro(error='El email ya está registrado')
        nuevo = Usuario(nombre, email, password)
        nuevo.save()
        return redirect(url_for('auth.login'))
    return auth_view.registro()

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

# Decorador para proteger rutas
def login_required(view):
    from functools import wraps
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view