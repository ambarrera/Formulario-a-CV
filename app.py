from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/principal',methods=["POST"])
def principal():
    name = request.form.get("name")
    last_name = request.form.get("last_name")
    born = request.form.get("born")
    occupation = request.form.get("occupation")
    phone = request.form.get("phone")
    email = request.form.get("email")
    nacionality = request.form.get("nacionality")
    english_level = request.form.get("english_level")
    programing_languagues = request.form.get("programing_languagues")
    aptitudes = request.form.get("aptitudes")
    habilities = request.form.get("habilities")
    perfil = request.form.get("perfil")


    return render_template("principal.html",
        nombre=name, 
        apellido=last_name,  
        ocupacion=occupation, 
        nacimiento=born, 
        numero = phone, 
        mail = email, 
        nacionalidad = nacionality,
        nivel_de_ingles = english_level,
        lenguajes_de_programacion = programing_languagues, 

        aptitudes = aptitudes, 
        habilidades = habilities, 
        perfil = perfil)