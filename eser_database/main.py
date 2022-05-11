import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.dialects.sqlite

BASEDIR = os.path.abspath(os.path.dirname(__name__))
print(f"Base directory: {BASEDIR}")

app = Flask(__name__)

# configurare il path del database e altre info
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

# aggiungiamo un istanza sqlalchemy all'app
db = SQLAlchemy(app)

# Definiamo corsi
class Lezione(db.Model):
    
    #nome tabella
    __tablename__ = "lezione"
    
    #definiamo la struttira della tabella
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    insegnante = db.Column(db.Text)
    allievi = db.Column(db.Integer)
    
    # definiamo il costruttore 
    def __init__(self, nome, insegnante, allievi):
        self.nome = nome
        self.insegnante = insegnante
        self.allievi = allievi
        
    # rappresentiamo l'oggetto stampato
    def __repr__(self):
        message = f"\n Corso: {self.nome} insegnato da: {self.insegnante} numero di allievi: {self.allievi} con id: {self.id}"
        return message