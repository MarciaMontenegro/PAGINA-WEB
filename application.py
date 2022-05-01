from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/") 
def inicio():
  return render_template("inicio.html")

@app.route("/productos") 
def productos():
  return render_template("productos.html")


@app.route("/login") 
def login():
  return render_template("Login.html")

@app.route("/register") 
def register():
  return render_template("Register.html")

@app.route("/cart") 
def cart():
  return render_template("Cart.html")
