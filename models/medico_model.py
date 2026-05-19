from database import db

class Medico(db.Model):
    __tablename__ = 'medicos'
    id_medico = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)

    consultas = db.relationship('Consulta', backref='medico', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Medico.query.all()

    @staticmethod
    def get_by_id(id):
        return Medico.query.get(id)

    def update(self, nombre, especialidad, telefono, correo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()