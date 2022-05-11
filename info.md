# Creare db
python3
from app import db
db.create_all()
# Config DB
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
