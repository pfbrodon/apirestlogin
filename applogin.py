from flask import Flask  ,request, render_template, Response, session, redirect
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_mysqldb import MySQL, MySQLdb
app=Flask(__name__, template_folder='template')  # crear el objeto app de la clase Flask


app.config['MYSQL_HOST']='pfbrodon.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER']='pfbrodon'
app.config['MYSQL_PASSWORD']='prueba1234'
app.config['MYSQL_DB']='pfbrodon$proyecto'
app.config['MYSQL_CURSORCLASS']='DictCursor'
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
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)