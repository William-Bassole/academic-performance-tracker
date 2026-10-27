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
    cours = charger_cours()
    evals = charger_evaluations()
    res = charger_resultats()

    menu = True
    while menu == True :
        choix = input("\nChoisissez un scénario : (0-5)\n\n\n-Scénario 1) Recherche d'un cours\n\n-Scénario 2) Cours en difficulté\n\n-Scénario 3) Moyennes\n\n-Scénario 4) Top 3 cours en difficulté avec objectifs\n\n-Scénario 5) Bilan\n\n-0) Quitter\n")
        if choix == "1" :
            recherche_cours(cours, evals, res)
        elif choix == "2" :
            cours_en_difficulte(cours, evals, res)
        elif choix == "3" :
            moyenne_semestre(cours, evals, res)
        elif choix == "4" :
            top3_cours_difficiles(cours, evals, res)
        elif choix == "5" :
            bilan_global(cours, evals, res)
        elif choix == "0" :
            print("\nAu revoir\n")
            menu = False
        else : print("\n\nVeuillez entrer un nombre entre 0 et 5\n\n\n")

   







# Scénarios

def recherche_cours(cours, evals, res):
    # TODO : scénario 1 - infos du cours, évaluations, notes et temps de préparation
    pass


def cours_en_difficulte(cours, evals, res):
    # TODO : scénario 2 - cours dont la moyenne actuelle est inférieure à 5
    pass


def moyenne_semestre(cours, evals, res):
    # TODO : scénario 3 - moyennes des cours et moyenne pondérée du semestre
    pass


def top3_cours_difficiles(cours, evals, res):
    # TODO : scénario 4 - les 3 moyennes les plus faibles, avec objectif et écart
    pass


def bilan_global(cours, evals, res):
    # TODO : scénario 5 - bilan croisant les 3 sources
    pass


if __name__ == '__main__':
    main()
