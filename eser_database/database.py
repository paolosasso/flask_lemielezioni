from main import db, Lezione


#Creazione delle tabelle
db.create_all()

# costruiamo i notri oggetti
lez_info = Lezione("Informatica","Davide Piccolo",20)
lez_mate = Lezione("Matematica", "Marco La Monica", 20)
lez_ing = Lezione("Inglese", "Marco Rossi",45)
lez_ita = Lezione("Italiano", "Maria Rinaldi", 56)
                  

# Aggiungiamo alla sessione del database i nostri oggetti
db.session.add(lez_info)
db.session.add(lez_mate)
db.session.add(lez_ing)
db.session.add(lez_ita)
db.session.commit()

# visualizziamo gli id
print(lez_ing)
print("id lezione matrematica: ", lez_mate.id)
print("id lezione matrematica: ", lez_ing.id)
print("id lezione matrematica: ", lez_ita.id)


