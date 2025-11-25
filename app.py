from flask import Flask, render_template
from config import config_by_name
from database import init_db
from routes.asistencia_bp import asistencia_bp
from routes.alumnos_bp import alumnos_bp
from routes.registro_bp import registro_bp
from routes.entrada_bp import entrada_bp
from routes.reportes_bp import reportes_bp
from routes.justificantes_bp import justificantes_bp
from flask import Flask, session
from routes.auth_bp import auth_bp




app = Flask(__name__)
app.secret_key = "RUTILIO23"  # ¡Cámbiala por algo seguro!

app = Flask(__name__)
app.config.from_object(config_by_name["development"])  # Aseguramos el entorno correcto

# Inicializa la base de datos
init_db(app)

# Registra los Blueprints
app.register_blueprint(asistencia_bp, url_prefix="/asistencia")
app.register_blueprint(alumnos_bp, url_prefix="/alumnos")
app.register_blueprint(registro_bp, url_prefix='/control')
app.register_blueprint(entrada_bp, url_prefix="/entrada")
app.register_blueprint(reportes_bp, url_prefix="/reportes")
app.register_blueprint(justificantes_bp, url_prefix="/justificantes")
app.register_blueprint(auth_bp, url_prefix="/auth")

# Ruta principal
@app.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error cargando la página de inicio: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
    