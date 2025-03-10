from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Url de la base de donnée
DATABASE_URL = "sqlite:///data/service_b.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modèle SQLite
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Créer la table au démarrage
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Session base de donnée
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add-item/")
def add_item(name: str, db: Session = Depends(get_db)):
    item = Item(name=name)
    db.add(item)
    db.commit()
    return {"message": f"Item '{name}' ajouté !"}

@app.get("/items/")
def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items
