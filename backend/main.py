import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# --- CONFIGURATION SÉCURITÉ (CORS) ---
# Autorise React (qui est sur un autre port) à parler à FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dans un vrai projet, on limiterait à l'URL du site
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODÈLES DE DONNÉES ---
class MusicData(BaseModel):
    note_jouee: str

# --- ROUTES (LES POINTS D'ACCÈS) ---

@app.get("/")
def read_root():
    return {"status": "En ligne", "message": "Serveur IA Musique prêt"}

# Route pour donner un exercice à l'utilisateur
@app.get("/get-lesson")
def get_lesson():
    notes_possibles = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
    # Choisit une note au hasard dans la liste
    note_cible = random.choice(notes_possibles)
    return {"note_a_jouer": note_cible}

# Route pour prédire/suggérer la note suivante (IA simple pour le moment)
@app.post("/predict")
async def predict_next_note(data: MusicData):
    notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
    try:
        idx = notes.index(data.note_jouee)
        # Suggère la note juste après (boucle au début si on est à la fin)
        prochaine = notes[(idx + 1) % len(notes)]
        return {"suggestion": prochaine}
    except ValueError:
        return {"suggestion": "C4"}