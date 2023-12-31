from flask import Flask ,jsonify ,request, render_template, url_for, redirect
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__,template_folder='template')  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/proyecto'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemyb ,cvgb                                    
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

@app.route('/producto_nuevo')
def producto_nuevo():
    return render_template('producto_nuevo.html')

@app.route('/producto_update')
def producto_update():
    return render_template('producto_update.html')


# defino las tablas
class Producto(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    cantidad=db.Column(db.Integer)
    categoria=db.Column(db.String(50))
    codigo=db.Column(db.Integer)
    descripcion=db.Column(db.String(50))
    precioUnit=db.Column(db.Integer)
    precioVPublico=db.Column(db.Integer)
    
    def __init__(self,cantidad,categoria,codigo,descripcion,precioUnit,precioVPublico):   #crea el  constructor de la clase
        self.cantidad=cantidad  # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.categoria=categoria
        self.codigo=codigo
        self.descripcion=descripcion
        self.precioUnit=precioUnit
        self.precioVPublico=precioVPublico
#########tabala Login###############
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    nombre=db.Column(db.String(45), nullable=False)
    tipouser=db.Column(db.String(14), nullable=False)
    
    def __init__(self,email,password,nombre,tipouser):   #crea el  constructor de la clase
        self.email=email  # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.password=password
        self.nombre=nombre
        self.tipouser=tipouser

##############################################

    #  si hay que crear mas tablas , se hace aqui
'''class Login(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    email=db.Column(db.String(45))
    password=db.Column(db.String(8))'''
    





with app.app_context():
    db.create_all()  # aqui crea todas las tablas


class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','cantidad','categoria','codigo','descripcion','precioUnit','precioVPublico')



producto_schema=ProductoSchema()            # El objeto producto_schema es para traer un producto
productos_schema=ProductoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto




# crea los endpoint o rutas (json)
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla
    

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro


@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()                     # confirma el delete
    return producto_schema.jsonify(producto) # me devuelve un json con el registro eliminado


@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente
    cantidad=request.json['cantidad']
    categoria=request.json['categoria']
    codigo=request.json['codigo']
    descripcion=request.json['descripcion']
    precioUnit=request.json['precioUnit']
    precioVPublico=request.json['precioVPublico']
    new_producto=Producto(cantidad,categoria,codigo,descripcion,precioUnit,precioVPublico)
    db.session.add(new_producto)
    db.session.commit() # confirma el alta
    return producto_schema.jsonify(new_producto)


@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
 

    producto.cantidad=request.json['cantidad']
    producto.categoria=request.json['categoria']
    producto.codigo=request.json['codigo']
    producto.descripcion=request.json['descripcion']
    producto.precioUnit=request.json['precioUnit']
    producto.precioVPublico=request.json['precioVPublico']
    
    db.session.commit()    # confirma el cambio
    return producto_schema.jsonify(producto)    # y retorna un json con el producto

######RESTAR CANTIDAD####################################################
@app.route('/productos/<id>' ,methods=['PUT'])
def update_productoCant(id):
    producto=Producto.query.get(id)
 

    producto.cantidad=request.json['cantidad']
    #producto.categoria=request.json['categoria']
    #producto.codigo=request.json['codigo']
    #producto.descripcion=request.json['descripcion']
    #producto.precioUnit=request.json['precioUnit']
    #producto.precioVPublico=request.json['precioVPublico']

##########################################################################
    db.session.commit()    # confirma el cambio
    return producto_schema.jsonify(producto)    # y retorna un json con el producto
##############login#################################
@app.route('/login', methods=['POST', 'GET'])
def login():    
    email = request.form['email']
    password = request.form['password']
   # tipouser= request.form['tipouser']
   
    #usuario_autenticado = Login.query.filter_by(email=email).first()
    usuario_autenticado = Login.query.filter_by(email=email, password=password).first()

    if usuario_autenticado: # and check_password_hash(usuario_autenticado.password, password):
        print(usuario_autenticado.tipouser)
        
        # Autenticación exitosa
        if usuario_autenticado.tipouser=='admin':
            return render_template('prueba.html', email=usuario_autenticado.nombre, producto=producto_schema)
        else:
            return render_template('cliente.html', email=usuario_autenticado.nombre, productos=ProductoSchema)

    else:
        # Credenciales incorrectas
        return render_template('index.html', mensaje="Usuario Incorrecto")


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000


