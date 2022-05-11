from flask import Flask, render_template, request, url_for, session, redirect
from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    SubmitField,
    BooleanField,
    RadioField,
    SelectField,
    TextAreaField
    
)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "sicuramentequestachiavesicurae"

@app.route("/")
def index():
  # oi = "Super!!"
#   return f"<h1>Ciao {oi}<h1>"
    return render_template ("base.html")

@app.route("/esempio/")
def esempio():
   #oi = "Super!!"
   #return f"<h1>Ciao {oi}<h1>"
   return render_template ("index-detail.html")

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


### semplice form
@app.route("/course/new/", methods=["GET"])
def new_course():
    lesson_name = request.args.get("lesson-name")
    teacher_name = request.args.get("teacher-name")
    return render_template(
        "course_new.html", lesson_name=lesson_name, teacher_name=teacher_name
    )

class FormCorsoBase(FlaskForm):
    lesson_name = StringField("Nome della lezione", validators=[DataRequired()])
    teacher_name = StringField("Insegnante")
    lesson_active = BooleanField("lezione attiva?")
    difficulty = RadioField(
        "Difficoltà del corso", choices=[(
            'facile','Facile'), ('medio', 'Medio'),('avanzato','Avanzato')],
    )
    platform = SelectField(
        u"Piattaforma lezione online", choices=[(
            'teams', 'Teams'),('zoom', 'Zomm'),('meet','Meet')]
    )
    feedback = TextAreaField("Note")
    submit = SubmitField("Submit")
    
# form avanzato
@app.route("/lesson/prova/", methods=["GET", "POST"])
def advance_form():
    lesson_name = False
    teacher_name  = False
    lesson_active = False
    difficulty = False
    platform = False
    feedback = False
    form = FormCorsoBase()
    
    # logica del form
    if form.validate_on_submit():
        session["lesson_name"] = form.lesson_name.data
        session["teacher_name"] = form.teacher_name.data
        session["lesson_active"] = form.lesson_active.data
        session["difficulty"] = form.difficulty.data
        session["platform"] = form.platform.data
        session["feedback"] = form.feedback.data
        
        # reset
        form.lesson_name.data = ""
        form.teacher_name.data = ""
        form.lesson_active.data = ""
        form.difficulty.data = ""
        form.platform.data = ""
        form.feedback.data = ""
    
        return redirect(url_for("lesson_created"))
        
    return render_template(
        "corso_simple.html", 
        lesson_simple_form=form,
        lesson=lesson_name, 
        teacher=teacher_name, 
        active=lesson_active,
        level=difficulty, 
        platform_online=platform,
        opinion=feedback, 
        
    )   

@app.route("/lesson/created/")
def lesson_created():
    #corso_name = ""
    #corso_subject = ""
    
    return render_template("corso_created.html")

if __name__ == "__main__":
    app.run(debug=True)