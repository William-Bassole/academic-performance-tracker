"""
Academic Performance Tracker - TP1 Mashup, Contextualisation et Qualité des Services
Auteur : William Bassole

Service local en ligne de commande qui combine 3 sources de données :
- data/cours.json        (cours : id, nom, ects, semestre, objectif)
- data/evaluations.xml   (évaluations : id, id_cours, type, coefficient)
- data/resultats.json    (résultats : id_evaluation, note, heures_preparation, date)
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


# ---------- 1. Chargement des sources ----------

def charger_cours():
    """Lit cours.json et retourne une liste de dictionnaires."""
    # TODO
    pass


def charger_evaluations():
    """Lit evaluations.xml et retourne une liste de dictionnaires
    (même structure que le JSON pour simplifier la suite)."""
    # TODO
    pass


def charger_resultats():
    """Lit resultats.json et retourne une liste de dictionnaires."""
    # TODO
    pass


# ---------- 2. Scénarios ----------

def scenario_recherche_cours():
    # TODO : scénario 1
    pass


def scenario_cours_en_difficulte():
    # TODO : scénario 2
    pass


def scenario_moyenne_semestre():
    # TODO : scénario 3
    pass


def scenario_top3_difficiles():
    # TODO : scénario 4
    pass


def scenario_bilan_global():
    # TODO : scénario 5
    pass


# ---------- 3. Menu ----------

def main():
    # Étape 1 : vérifier que le chargement fonctionne
    print(charger_cours())
    print(charger_evaluations())
    print(charger_resultats())

    # Étape 2 (plus tard) : boucle avec le menu des 5 scénarios + Quitter


if __name__ == "__main__":
    main()
