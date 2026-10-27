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
def trouver_resultat(id_evaluation, res):
    for resultat in res:
        if resultat["id_evaluation"] == id_evaluation:
            return resultat
    return None
 
def moyenne_cours(id_cours, evals, res):
    somme = 0
    somme_coef = 0
    for evaluation in evals:
        if evaluation["id_cours"] == id_cours:
            resultat = trouver_resultat(evaluation["id"], res)
            if resultat != None:
                somme = somme + resultat["note"] * evaluation["coefficient"]
                somme_coef = somme_coef + evaluation["coefficient"]
    if somme_coef == 0:
        return None
    return somme / somme_coef

def recherche_cours(cours, evals, res):
    recherche = input("\nIdentifiant ou nom du cours : ")
    trouve = None
    for c in cours:
        if c["id"] == recherche or recherche in c["nom"]:
            trouve = c
    if trouve == None:
        print("Aucun cours n'a été trouvé.\n")
        return
 
    print(f"\n{trouve['nom']} ({trouve['id']}) - {trouve['ects']} ECTS - {trouve['semestre']}")
    print(f"Objectif : {trouve['objectif']}")
    total_heures = 0
    for evaluation in evals:
        if evaluation["id_cours"] == trouve["id"]:
            resultat = trouver_resultat(evaluation["id"], res)
            if resultat == None:
                print(f"  {evaluation['id']} {evaluation['type']} (coef {evaluation['coefficient']}) : pas encore de note")
            else:
                print(f"  {evaluation['id']} {evaluation['type']} (coef {evaluation['coefficient']}) : {resultat['note']} - {resultat['heures_preparation']} h - {resultat['date']}")
                total_heures = total_heures + resultat["heures_preparation"]
    moyenne = moyenne_cours(trouve["id"], evals, res)
    if moyenne == None:
        print("Moyenne actuelle : aucune note")
    else:
        print(f"Moyenne actuelle : {moyenne:.2f}")
    print(f"Temps de préparation total : {total_heures} h\n")


def cours_en_difficulte(cours, evals, res):
    print("\nCours avec une moyenne inférieure à 5 :")
    nb = 0
    for c in cours:
        moyenne = moyenne_cours(c["id"], evals, res)
        if moyenne != None and moyenne < 5:
            print(f"  {c['nom']} : {moyenne:.2f} (objectif {c['objectif']})")
            nb = nb + 1
    if nb == 0:
        print("Vous n'avez aucun cours en difficulté.")
    print()


def moyenne_semestre(cours, evals, res):
    semestres = []
    for c in cours:
        if c["semestre"] not in semestres:
            semestres.append(c["semestre"])
    print("Semestres disponibles :")
    for i in range(len(semestres)):
        print(f"  {i + 1}) {semestres[i]}")
    choix = input("Choisissez un semestre : ")
    if choix == "1":
        semestre = semestres[0]
    elif choix == "2":
        semestre = semestres[1]
    else:
        print("Choisissez un semestre valide (1-2)\n")
        return
 
    print(f"\nMoyennes - {semestre}")
    somme = 0
    somme_ects = 0
    for c in cours:
        if c["semestre"] == semestre:
            moyenne = moyenne_cours(c["id"], evals, res)
            if moyenne == None:
                print(f"  {c['nom']} : pas encore de note")
            else:
                print(f"  {c['nom']} : {moyenne:.2f} ({c['ects']} ECTS)")
                somme = somme + moyenne * c["ects"]
                somme_ects = somme_ects + c["ects"]
    if somme_ects == 0:
        print("Moyenne du semestre : aucune note\n")
    else:
        print(f"Moyenne du semestre : {somme / somme_ects:.2f}\n")


def top3_cours_difficiles(cours, evals, res):
    classement = []
    for c in cours:
        moyenne = moyenne_cours(c["id"], evals, res)
        if moyenne != None:
            classement.append((moyenne, c["id"]))
    classement.sort()
    
    
    print("\nTop 3 des cours les plus difficiles :")
    for i in range(min(3, len(classement))):
        moyenne = classement[i][0]
        for c in cours:
            if c["id"] == classement[i][1]:
                ecart = moyenne - c["objectif"]
                print(f"  {i + 1}. {c['nom']} : {moyenne:.2f} / objectif {c['objectif']} (écart {ecart:+.2f})")
    print()


def bilan_global(cours, evals, res):
    print("\nBilan global")
    for c in cours:
        nb_evals = 0
        heures = 0
        for evaluation in evals:
            if evaluation["id_cours"] == c["id"]:
                resultat = trouver_resultat(evaluation["id"], res)
                if resultat != None:
                    nb_evals = nb_evals + 1
                    heures = heures + resultat["heures_preparation"]
        moyenne = moyenne_cours(c["id"], evals, res)
        if moyenne == None:
            texte_moyenne = "-"
        else:
            texte_moyenne = f"{moyenne:.2f}"
        print(f"  {c['nom']}")
        print(f"     moyenne {texte_moyenne} ; objectif {c['objectif']} ; {c['ects']} ECTS ; {nb_evals} évaluation(s) notée(s) ; {heures} h de préparation")
    


if __name__ == '__main__':
    main()
