from flask import Blueprint, request, redirect, url_for
from models.paciente_model import Paciente
import views.paciente_view as paciente_view
from controllers.auth_controller import login_required

paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes')

@paciente_bp.route('/')
@login_required
def index():
    pacientes = Paciente.get_all()
    return paciente_view.list(pacientes)

@paciente_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        paciente = Paciente(
            nombre=request.form['nombre'],
            edad=request.form['edad'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono']
        )
        paciente.save()
        return redirect(url_for('paciente.index'))
    return paciente_view.create()

@paciente_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    paciente = Paciente.get_by_id(id)
    if request.method == 'POST':
        paciente.update(
            nombre=request.form['nombre'],
            edad=request.form['edad'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono']
        )
        return redirect(url_for('paciente.index'))
    return paciente_view.edit(paciente)

@paciente_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    paciente = Paciente.get_by_id(id)
    paciente.delete()
    return redirect(url_for('paciente.index'))