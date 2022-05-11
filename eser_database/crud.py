## ESEMPIO CRUD
# CREATE 
# READ (SELECT)
# UPDATE
# DELETE

from main import db, Lezione

## CREATE
#lez_fis = Lezione("Fisica", "Marina Siniscalchi", 15)
#lez_mus = Lezione("Musica", "Serena Rossi", 30)
#db.session.add_all([lez_fis,lez_mus])
#db.session.commit()

# READ tutti i corsi
#tutte_lezioni = Lezione.query.all()
#print(tutte_lezioni)

""" SELECT (READ) corso tramite id e nome
lezione_selez = Lezione.query.get(6)
lezione_selez1 = Lezione.query.get(34)
lezione_selez3 = Lezione.query.get(8)


print(lezione_selez)
print(lezione_selez1)
print(lezione_selez3)
"""

# FILTRO
#lezione_selezionata_nome = Lezione.query.filter_by(nome="Informatica")
#print(lezione_selezionata_nome) # ritorna la query
#print(lezione_selezionata_nome.first()) # ritorna il primo risultato trovato
#print(lezione_selezionata_nome.all()) # ritorna i risultati trovati

# AGGIORNAMENTO
#lez_ita = Lezione.query.get(8)
#lez_ita.allievi = 45
#db.session.add(lez_ita)
#db.session.commit()
#print(Lezione.query.get(8))

# DELETE
lezione_da_rimuovere = Lezione.query.filter_by(nome="Musica").all()
db.session.delete(lezione_da_rimuovere[-1])
db.session.commit()
print(Lezione.query.all())
