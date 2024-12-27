from flask import Flask, render_template, redirect , url_for, request, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import  CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

#* Model User
from models.ModelUser import ModelUser

#* Entities
from models.entities.User import User


app = Flask(__name__)
db  = MySQL(app)
csrf = CSRFProtect()
login_manager


@app.route('/')
def principal():
    return redirect( url_for("login"))

@app.route('/login', methods = ["GET","POST"])
def login():

    if request.method == "POST":

        user = User(0,request.form["username"],request.form["password"])
        
        logged_user = ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.password:

                return redirect(url_for("home"))

            else:
                flash ("Contraseña erronea")
                return render_template("login.html")


        else:
             flash("Usuario no encontrado ome")
             return render_template("login.html")

       

    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == "__main__":

    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.run()

