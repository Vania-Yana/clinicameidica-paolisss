from flask import render_template

def list(consultas, fecha_filtro):
    return render_template('consulta/index.html', consultas=consultas, fecha_filtro=fecha_filtro)

def create(medicos, pacientes):
    return render_template('consulta/create.html', medicos=medicos, pacientes=pacientes)

def edit(consulta, medicos, pacientes):
    return render_template('consulta/edit.html', consulta=consulta, medicos=medicos, pacientes=pacientes)