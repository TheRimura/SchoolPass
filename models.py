from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Alumno(db.Model):
    __tablename__ = "alumnos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True)  # 🔐 Campo para ocultar lógicamente

    def __repr__(self):
        return f"<Alumno {self.nombre} {self.apellido} - {self.matricula}>"

# 📋 Tabla de asistencia general
class Asistencia(db.Model):
    __tablename__ = "asistencia"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey("alumnos.id"), nullable=False)
    hora_entrada = db.Column(db.DateTime, nullable=False)
    hora_salida = db.Column(db.DateTime, nullable=True)

# 🚻 Tabla nueva para registro de salidas al baño
class RegistroBaño(db.Model):
    __tablename__ = "registro_banio"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey("alumnos.id"), nullable=False)

    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)

    fecha = db.Column(db.Date, default=datetime.now().date, nullable=False)
    hora_salida = db.Column(db.Time)
    hora_regreso = db.Column(db.Time)

    alumno = db.relationship("Alumno", backref="registros_banio")

    def __repr__(self):
        return f"<SalidaBaño {self.nombre} {self.apellido} - {self.fecha}>"
    
class RegistroAsistencia(db.Model):
    __tablename__ = "registro_asistencia"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey("alumnos.id"), nullable=False)

    nombre    = db.Column(db.String(100), nullable=False)
    apellido  = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)

    fecha         = db.Column(db.Date, default=datetime.now().date, nullable=False)
    hora_entrada  = db.Column(db.Time)
    hora_salida   = db.Column(db.Time)

    alumno = db.relationship("Alumno", backref="registros_asistencia")

    def __repr__(self):
        return f"<Asistencia {self.nombre} {self.apellido} - {self.fecha}>"
    
class HistorialReportes(db.Model):
    __tablename__ = "historial_reportes"

    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey("alumnos.id"), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)
    total_reportes = db.Column(db.Integer, default=0)

    alumno = db.relationship("Alumno", backref="reporte_historial")

    def __repr__(self):
        return f"<Reportes {self.nombre} {self.apellido}: {self.total_reportes}>"
    


class User(db.Model):
    __tablename__ = "users"

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre        = db.Column(db.String(100), nullable=False)
    apellido      = db.Column(db.String(100), nullable=False)
    email         = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"    
    
