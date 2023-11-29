from flask import Flask, request, render_template, Response, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__,template_folder='template')

###############################BASE EXTERNA##################################################################
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://pfbrodon:prueba1234@pfbrodon.mysql.pythonanywhere-services.com/pfbrodon$proyecto'
## URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
#############################################################################################################

###############################BASE LOCAL####################################################################
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/proyecto'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
##############################################################################################################
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma= Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)

from werkzeug.security import check_password_hash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login', methods=['GET','POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    usuario_autenticado = Login.query.filter_by(email=email).first()

    if usuario_autenticado: # and check_password_hash(usuario_autenticado.password, password):
        # Autenticación exitosa
        return render_template('bienvenida.html', email=usuario_autenticado.email)
    else:
        # Credenciales incorrectas
        return render_template('index.html')
    
if __name__=='__main__':
    app.run(debug=True, port=5000)