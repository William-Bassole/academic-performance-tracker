import json
import xml.etree.ElementTree as ET


# Chargement des sources

FICHIER_COURS = "data/cours.json"
FICHIER_EVALUATIONS = "data/evaluations.xml"
FICHIER_RESULTATS = "data/resultats.json"

def charger_cours():
    with open(FICHIER_COURS) as file:
        data = json.load(file)
    return data["cours"]

def charger_evaluations():
    with open(FICHIER_EVALUATIONS) as file:
        tree = ET.parse(file)
        root = tree.getroot()
        evaluations = []
        for item in root:
            evaluation = {}
            evaluation["id"] = item.get("id")
            for child in item:
                evaluation[child.tag] = child.text
            evaluation["coefficient"] = float(evaluation["coefficient"])
            evaluations.append(evaluation)
    return evaluations

def charger_resultats():
    with open(FICHIER_RESULTATS) as file:
        data = json.load(file)
    return data["resultats"]


# Menu 

def main():
    charger_cours()
    charger_evaluations()
    charger_resultats()

# if __name__ == "__main__":
#     main()
#     menu = true 
#     while menu == true :
#         print("Choisissez un scénario : (1-5)")







# Scénarios

def recherche_cours():
    # TODO : scénario 1 - infos du cours, évaluations, notes et temps de préparation
    pass


def cours_en_difficulte():
    # TODO : scénario 2 - cours dont la moyenne actuelle est inférieure à 5
    pass


def moyenne_semestre():
    # TODO : scénario 3 - moyennes des cours et moyenne pondérée du semestre
    pass


def top3_cours_difficiles():
    # TODO : scénario 4 - les 3 moyennes les plus faibles, avec objectif et écart
    pass


def bilan_global():
    # TODO : scénario 5 - bilan croisant les 3 sources
    pass


