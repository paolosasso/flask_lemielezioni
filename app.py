#from operator import le 
from flask import Flask, redirect, render_template, render_template_string, url_for , request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    SubmitField
)
from flask_simplelogin import SimpleLogin
from flask_simplelogin import is_logged_in





#import requests

app = Flask(__name__)

app.config["SECRET_KEY"] = "sicuramentequestachiavesicurae"

# configurare il path del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'

# aggiungiamo un istanza sqlalchemy all'app
db = SQLAlchemy(app)

# Import Migrations
from flask_migrate import Migrate, migrate

# Configuriamo la migrazione
migrate = Migrate(app, db)
app.config['SIMPLELOGIN_USERNAME'] = 'chuck'
app.config['SIMPLELOGIN_PASSWORD'] = 'norris'
SimpleLogin(app)

# Definiamo corsi
class Lezione(db.Model):

    #nome tabella
    __tablename__ = "Lezione"

    #definiamo la struttira della tabella
    id = db.Column(db.Integer, primary_key=True)
    lesson_name = db.Column(db.Text)
    teacher_name = db.Column(db.Text)

    # definiamo il costruttore
    def __init__(self, lesson_name, teacher_name):
        self.lesson_name = lesson_name
        self.teacher_name = teacher_name

    # rappresentiamo l'oggetto stampato
    def __repr__(self):
        message = f"\n Corso: {self.lesson_name} insegnato da: {self.teacher_name} con id: {self.id}"
        return message

#@app.route("/")
#def index():
  # oi = "Super!!"
#   return f"<h1>Ciao {oi}<h1>"
#    return render_template ("base.html")

@app.route("/")
def index():
    lezioni = Lezione.query.all()
    return render_template ("index-detail.html", lezioni=lezioni )

@app.route("/admin")
def index_admin():
    if is_logged_in():
        lezioni = Lezione.query.all()
        return render_template ("index-admin.html", lezioni=lezioni )
    else:
        return render_template ("404.html"), 404

@app.route("/corso/<name>")
def corso_flask(name):
    lista_scuole_sup = ["liceo","tecnico","professionale"]
    return render_template ("corso-flask.html",nome_scuola=name,pag_delle_superiori=lista_scuole_sup)

@app.route("/info/")
def info():
    return f"<h2>Queste sono belle info<h2>"

@app.route("/info/<name>")#127.0.0.1:5000/info/andrea
def nome_ok(name):
    return f"<h2>Il mio nome: {name} <h2>"

#@app.route("/info-errore/<name>")
@app.errorhandler(404)
def page_not_found(error):
 #   return f"<h2>Generiamo un errore:<h2>".format(name[9])
    return render_template ("404.html"), 404

"""
@app.route("/course/created/")
def course_created():
    corso_name = ""
    corso_subject = ""
    return render_template("course_created.html", corso_name=corso_name,
    corso_subject=corso_subject)
"""

### semplice form
@app.route("/course/new/",methods=["GET", "POST"])
def new_course():
    lesson_name = request.args.get("lesson-name")
    teacher_name = request.args.get("teacher-name")
    return render_template(
       "course_new.html" , lesson_name=lesson_name, teacher_name=teacher_name)
    


### form avanzato
class FormLezioneBase(FlaskForm):
    lesson_name = StringField("Nome della lezione")
    teacher_name = StringField("Insegnante")
    submit = SubmitField("Submit")

@app.route("/lezione/prova/", methods=["GET", "POST"])
def advance_form():
    lesson_name = False
    teacher_name  = False
    form = FormLezioneBase()

    # logica del form
    if form.validate_on_submit():
        lesson_name = form.lesson_name.data
        teacher_name = form.teacher_name.data
        
        #add db session
        l = Lezione(lesson_name=lesson_name, teacher_name=teacher_name)
        db.session.add(l)
        
        #reset
        form.lesson_name.data = ""
        form.teacher_name.data = ""
        
        #commit
        db.session.commit()
        
        return redirect('/')

    
    return render_template(
        "lezione.html",
        lesson_form=form,
        #lesson=lesson_name,
        #teacher=teacher_name,

        )



@app.route('/delete/<int:id>')
def cancella(id):
     
    # deletes the data on the basis of unique id and
    # directs to home page
    l = Lezione.query.get(id)
    db.session.delete(l)
    db.session.commit()
    return redirect('/')


""" create the app for access free api

url = "http://universities.hipolabs.com/search?country=Italy"

response = requests.get(url)

@app.route("/univers/list/")
def show_univers():
    univers = response.json()
    return render_template("show_university.html", univers = univers)

"""
if __name__ == "__main__":
    app.run(debug=True)