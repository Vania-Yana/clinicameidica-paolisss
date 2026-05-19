from flask import Blueprint, request, redirect, url_for, render_template
from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente
import views.consulta_view as consulta_view
from controllers.auth_controller import login_required
from datetime import datetime

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consultas')

@consulta_bp.route('/')
@login_required
def index():
    # Filtro por fecha (extra)
    fecha_str = request.args.get('fecha')
    if fecha_str:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        consultas = Consulta.query.filter(db.func.date(Consulta.fecha) == fecha).all()
    else:
        consultas = Consulta.get_all()
    return consulta_view.list(consultas, fecha_str)

@consulta_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
        consulta = Consulta(
            fecha=fecha,
            diagnostico=request.form['diagnostico'],
            tratamiento=request.form['tratamiento'],
            id_medico=request.form['id_medico'],
            id_paciente=request.form['id_paciente']
        )
        consulta.save()
        return redirect(url_for('consulta.index'))
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    return consulta_view.create(medicos, pacientes)

@consulta_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    consulta = Consulta.get_by_id(id)
    if request.method == 'POST':
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
        consulta.update(
            fecha=fecha,
            diagnostico=request.form['diagnostico'],
            tratamiento=request.form['tratamiento'],
            id_medico=request.form['id_medico'],
            id_paciente=request.form['id_paciente']
        )
        return redirect(url_for('consulta.index'))
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    return consulta_view.edit(consulta, medicos, pacientes)

@consulta_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    consulta = Consulta.get_by_id(id)
    consulta.delete()
    return redirect(url_for('consulta.index'))