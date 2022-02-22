# OpenClassRoom - Projet 4 - Manager de tournoi d'echec

Ce projet a pour but de créer un logiciel permettant de gerer des tournoi d'échec, en créant des tournoi et des joueurs, changer leur classement et générer des rapports

# Utilisation

## Environnement virtuel

Pour mettre en place l'environnement virtuel nécessaire pour faire fonctionner le script, procéder comme suit :

Dans un terminal ouvert dans le dossier où vous avez cloné le repository, créez un environnement virtuel a l'aide de 
venv :

```bash
python3 -m venv [nom environnement]
```

Une fois que l'environnement est créé, activez l'environnement (dans cet exemple, 'env' est le nom de mon environnement) :

Windows

```bash
.\env\Scripts\activate
```

Mac / Linux 

```bash
source env/bin/activate
```

Si l'environnement c'est bien activé, le nom de l'environnement s'affichera à gauche de l'indicateur de position 
dans le terminal

Installez tout les packages listé dans le fichier 'requirements.txt' dans votre environnement virtuel :

```bash
pip install -r requirements.txt
```

Vérifier que tout les packages sont bien installé a l'aide de la commande `pip freeze`.

## Lancement

Dans un terminal ouvert dans le dossier du logiciel, assurez vous d'activer l'environnement virtuel avec la commande :

Windows

```bash
.\env\Scripts\activate
```

Mac / Linux 

```bash
source env/bin/activate
```

Puis, entrez la commande :

```bash
python app.py
```



## Génération Rapport Flake8

Après avoir activé l'environnement virtuel, entrez la commande suivante :

```bash
flake8
```

Grâce au fichier de configuration .flake8 un rapport html sera généré dans le dossier "flake_rapport"
