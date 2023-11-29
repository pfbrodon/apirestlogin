from flask import Flask  ,request, render_template, Response, session, redirect
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__, template_folder='template')  # crear el objeto app de la clase Flask

###########################################################################
app.config['MYSQL_HOST']='pfbrodon.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER']='pfbrodon'
app.config['MYSQL_PASSWORD']='prueba1234'
app.config['MYSQL_DB']='pfbrodon$proyecto'
app.config['MYSQL_CURSORCLASS']='DictCursor'
############################################################################
#app.config['MYSQL_HOST']='localhost'
#app.config['MYSQL_USER']='root'
#app.config['MYSQL_PASSWORD']='root'
#app.config['MYSQL_DB']='proyecto'
#app.config['MYSQL_CURSORCLASS']='DictCursor'
#############################################################################
## configuro la base de datos, con el nombre el usuario y la clave
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://pfbrodon:prueba1234@pfbrodon.mysql.pythonanywhere-services.com/pfbrodon$proyecto'
## URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
#db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
#ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow
#############################################################################
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


#FUNCION LOGIN
@app.route('/acceso-login', methods =["GET","POST"])
def login():
    if request.method =='POST' and 'txtCorreo' in request.form and 'txtPassword':
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM login WHERE email = %s AND password = %s',(_correo,_password,))
        account= cur.fetchone()
        if account:
            session['logueado']= True
            session['id']= account['id']
            return render_template("admin.html")
        else:
            return render_template('index.html', mensaje="Usuario Incorrecto")
        
if __name__=='__main__':
    app.secret_key="adminbuloneria"
    app.run(debug=True, port=5000, threaded=True)