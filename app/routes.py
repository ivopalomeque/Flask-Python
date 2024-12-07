from flask import render_template,make_response, abort,jsonify, Blueprint
from tabulate import tabulate
bp = Blueprint("routes", __name__)

@bp.route('/')
def home():
  return "Hola mundo ! "

@bp.route('/productos')
def productos():
  productos = [
    ["P001", "Laptop", 750, "✅"],
    ["P002", "Smartphone", 500, "❌"],
    ["P003", "Tablet", 300, "✅"],
  ]
  tabla_productos = tabulate(productos, headers=["Código", "Nombre", "Precio", "Stock"], tablefmt="html")
  return render_template("productos.html", tabla_productos=tabla_productos)

@bp.route('/saludo/<nombre>')
def saludo(nombre):
  return f"Hola {nombre}, como estas? ", 201

@bp.route('/plantilla/<nombre>')
def plantilla(nombre):
  return render_template("template.html", nombre=nombre)

@bp.route('/emojis')
def emojis():
  lista_emojis = ["😀", "🎉", "🚀", "🐍", "✨"]
  return render_template("template.html", emojis=lista_emojis)

@bp.route('/api')
def api():
  return make_response(jsonify({
    "status": "éxito",
    "message": "Hola desde la API !"
  }), 201 )

@bp.route('/estado/<estado>')
def estado_usuario(estado):
  return render_template("estado.html", estado=estado)

@bp.route('/dividirPor0')
def division_zero():
  try:
    resultado = 10/0
    return f"Dividir por cero es: {resultado}"
  except ZeroDivisionError:
    abort(500)

@bp.route('/rutaConAuth')
def rutaConAuth():
  try:
    loggedUser = True
    if not loggedUser:
      raise PermissionError("Acceso Dengeda2")
    return "Acceso Permiti3"
  except PermissionError:
    abort(403)