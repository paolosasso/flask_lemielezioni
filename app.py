#from operator import le 
from flask import Flask, redirect, render_template, render_template_string, url_for , request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    SubmitField,
    IntegerField
)
from flask_simplelogin import SimpleLogin
from flask_simplelogin import is_logged_in
import os
from dotenv import load_dotenv

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

load_dotenv()

user = os.environ['USER']
passw = os.environ['PASSW']

app.config['SIMPLELOGIN_USERNAME'] = user
app.config['SIMPLELOGIN_PASSWORD'] = passw
SimpleLogin(app)

# Definiamo corsi
class Lezione(db.Model):

    #nome tabella
    __tablename__ = "Lezione"

    #definiamo la struttira della tabella
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    click = db.Column(db.Integer)
    cps = db.Column(db.Integer)

    # definiamo il costruttore
    def __init__(self, nome, click, cps):
        self.nome = nome
        self.click = click
        self.cps = cps

    # rappresentiamo l'oggetto stampato
    def __repr__(self):
        message = f"\n Nome: {self.nome} Click: {self.click} CPS: {self.cps}"
        return message

@app.route("/leaderboard")
def index():
    lezioni = Lezione.query.all()
    return render_template ("leaderboard.html", lezioni=lezioni )

@app.route("/admin")
def index_admin():
    if is_logged_in():
        lezioni = Lezione.query.all()
        return render_template ("leaderboard_admin.html", lezioni=lezioni )
    else:
        return render_template ("404.html"), 404

#@app.route("/info-errore/<name>")
@app.errorhandler(404)
def page_not_found(error):
 #   return f"<h2>Generiamo un errore:<h2>".format(name[9])
    return render_template ("404.html"), 404

class FormLezioneBase(FlaskForm):
    nome = StringField("Nome")
    click = IntegerField("Click")
    cps = IntegerField("CPS")
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def advance_form():
    nome = False
    click  = False
    cps = False
    form = FormLezioneBase()

    # logica del form
    if form.validate_on_submit():
        nome = form.nome.data
        click = form.click.data
        cps = form.cps.data
    
        #add db session
        l = Lezione(nome=nome, click=click, cps=cps)
        db.session.add(l)
        
        #reset
        form.nome.data = ""
        form.click.data = ""
        form.cps.data = ""
        
        #commit
        db.session.commit()
        
        return redirect('/')

    
    return render_template(
        "index.html",
        lesson_form=form,
        #lesson=lesson_name,
        #teacher=teacher_name,

        )


@app.route('/delete/<int:id>')
def cancella(id):
    if is_logged_in():
    # deletes the data on the basis of unique id and
    # directs to home page
        l = Lezione.query.get(id)
        db.session.delete(l)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/404')

if __name__ == "__main__":
    app.run(debug=True)