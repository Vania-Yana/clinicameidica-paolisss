from flask import render_template

def login(error=None):
    return render_template('auth/login.html', error=error)

def registro(error=None):
    return render_template('auth/registro.html', error=error)