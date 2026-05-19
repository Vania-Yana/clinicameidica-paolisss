import os
from flask import Flask, redirect, url_for
from database import db
from controllers.auth_controller import auth_bp
from controllers.medico_controller import medico_bp
from controllers.paciente_controller import paciente_bp
from controllers.consulta_controller import consulta_bp
from models.usuario_model import Usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///clinica.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'clave-secreta-para-session'

db.init_app(app)


app.register_blueprint(auth_bp)
app.register_blueprint(medico_bp)
app.register_blueprint(paciente_bp)
app.register_blueprint(consulta_bp)

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
