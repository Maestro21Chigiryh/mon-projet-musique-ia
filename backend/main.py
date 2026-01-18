from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importation de la sécurité

app = FastAPI()

# Configuration du CORS : c'est comme donner une clé à React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # On autorise tout le monde pour le moment
    allow_methods=["*"], # On autorise tous les types de requêtes (GET, POST...)
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Salut ! L'IA est prête à t'écouter."}