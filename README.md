# Academic Performance Tracker
 
Ce programme analyse la progression d'un étudiant à partir de données universitaires fictives (générées par claude.ia). Il croise trois sources (deux fichiers JSON et un fichier XML) pour :
 - calculer des moyennes 
 - repérer les cours en difficulté
 - comparer les résultats aux objectifs fixés pour chaque cours.

 
## Utilisation
 
Le programme ne requiert que Python 3, Les modules pour traiter Json et XML sont dans la bibliothèque standard, il n'y a donc rien de supplémentaire à installer.
 
Le programme doit être lancé depuis le dossier du projet, afin que les chemins de données correspondent.
 
```bash
cd academic-performance-tracker
python3 main.py
```
 
Un menu s'affiche : 

```
Choisissez un scénario : (0-5)
-Scénario 1) Recherche d'un cours
-Scénario 2) Cours en difficulté
-Scénario 3) Moyennes
-Scénario 4) Top 3 cours en difficulté avec objectifs
-Scénario 5) Bilan
-0) Quitter
```
On entre le numéro du scénario souhaité. Après chaque scénario, le menu réapparaît. `0` quitte le programme, et toute autre entrée affiche un message d'erreur sans arrêter le programme.
  

## Scénarios
 
### Scénario 1 : recherche d'un cours
 
L'utilisateur tape l'identifiant d'un cours ou son nom, le programme affiche : les informations du cours, chacune de ses évaluations avec sa note, son temps de préparation et sa date, puis la moyenne actuelle et le total d'heures de préparation. Si aucun cours ne correspond, un message l'indique.
 
Sources et données utilisées :
- `cours.json` : `id`, `nom`, `ects`, `semestre`, `objectif`
- `evaluations.xml` : `id`, `id_cours`, `type`, `coefficient`
- `resultats.json` : `id_evaluation`, `note`, `heures_preparation`, `date`

 
### Scénario 2 : cours en difficulté
 
Le programme calcule la moyenne actuelle de chaque cours et affiche ceux dont la moyenne est inférieure à 5, avec leur objectif.
 
Sources et données utilisées :
- `cours.json` : `id`, `nom`, `objectif`
- `evaluations.xml` : `id`, `id_cours`, `coefficient`
- `resultats.json` : `id_evaluation`, `note`
 
 
### Scénario 3 : moyenne d'un semestre
 
Le programme affiche la liste des semestres présents dans les données, puis l'utilisateur en choisit un. Il affiche la moyenne de chaque cours du semestre et la moyenne du semestre pondérée par les ECTS.
 
Sources et données utilisées :
- `cours.json` : `id`, `nom`, `ects`, `semestre`
- `evaluations.xml` : `id`, `id_cours`, `coefficient`
- `resultats.json` : `id_evaluation`, `note`

 
### Scénario 4 : top 3 des cours les plus difficiles
 
Le programme classe les cours de la moyenne la plus faible à la plus élevée et affiche les trois premiers, avec leur objectif et l'écart entre la moyenne et l'objectif.
 
Sources et données utilisées :
- `cours.json` : `id`, `nom`, `objectif`
- `evaluations.xml` : `id`, `id_cours`, `coefficient`
- `resultats.json` : `id_evaluation`, `note`

 
### Scénario 5 : bilan global
 
Pour chaque cours, le programme affiche la moyenne actuelle, l'objectif, les crédits ECTS, le nombre d'évaluations notées et le total d'heures de préparation. C'est le scénario qui utilise le plus d'éléments des trois sources à la fois.
 
Sources et données utilisées :
- `cours.json` : `id`, `nom`, `ects`, `objectif`
- `evaluations.xml` : `id`, `id_cours`, `coefficient`
- `resultats.json` : `id_evaluation`, `note`, `heures_preparation`

