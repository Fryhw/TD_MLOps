from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import sqlite3
from pydantic import BaseModel

app = FastAPI()

# Configuration de l'authentification basique
security = HTTPBasic()

# Connexion à la base de données SQLite
DATABASE = "database.db"

# Modèle Pydantic pour la validation des données
class Item(BaseModel):
    name: str

# Fonction pour vérifier les identifiants de l'admin
def authenticate_admin(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"  # En production, utilisez un mot de passe sécurisé et hashé
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Créer la table si elle n'existe pas
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Endpoint pour ajouter un nom (public)
@app.post("/add/")
def add_item(item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (?)", (item.name,))
    conn.commit()
    conn.close()
    return {"message": "Item added successfully"}

# Endpoint pour lire un nom par ID (protégé par authentification)
@app.get("/read/{item_id}")
def read_item(item_id: int, username: str = Depends(authenticate_admin)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    conn.close()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item["id"], "name": item["name"]}

# Initialiser la base de données au démarrage
init_db()