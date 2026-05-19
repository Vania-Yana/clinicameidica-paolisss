from flask import Blueprint, request, redirect, url_for
from models.medico_model import Medico
import views.medico_view as medico_view
from controllers.auth_controller import login_required

medico_bp = Blueprint('medico', __name__, url_prefix='/medicos')

@medico_bp.route('/')
@login_required
def index():
    medicos = Medico.get_all()
    return medico_view.list(medicos)

@medico_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        medico = Medico(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad'],
            telefono=request.form['telefono'],
            correo=request.form['correo']
        )
        medico.save()
        return redirect(url_for('medico.index'))
    return medico_view.create()

@medico_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    medico = Medico.get_by_id(id)
    if request.method == 'POST':
        medico.update(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad'],
            telefono=request.form['telefono'],
            correo=request.form['correo']
        )
        return redirect(url_for('medico.index'))
    return medico_view.edit(medico)

@medico_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    medico = Medico.get_by_id(id)
    medico.delete()
    return redirect(url_for('medico.index'))