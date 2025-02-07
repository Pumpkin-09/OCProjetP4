# OpenClassrooms projet 4: Logiciel de tournoi d’échecs

## Description
Ce code génère un programme autonome et hors ligne et se lance depuis la console.
Cette application permet de:
- Créer puis de gérer une base de données de joueur.
- Créer puis gérer des tournois d’échecs.
- Afficher un résumer de la base de données des joueurs ainsi que des différents tournois et de leurs informations respective.

## Installation
### Python
Si Python n'est pas installé, utilisez la documentation suivante en fonction de votre environnement:

[windows](https://docs.python.org/fr/3/using/windows.html)

[linux](https://docs.python.org/fr/3/using/unix.html) 

[mac](https://docs.python.org/fr/3/using/mac.html)

### Le projet
Ouvrez votre terminal, placez-vous dans le dossier de votre choix avec la commande cd puis clonez le repository:

`git clone https://github.com/Pumpkin-09/OCProjetP4.git`

Placez vous ensuite dans le dossier OCProjetP4, toujours avec la commande cd, vous allez créer puis activer votre environnement virtuel. 
#### Utilisez les commandes suivantes:
##### Sous linux et mac:

`python3 -m venv env`

pour la création de l'environnement, puis:

`source env/bin/activate`

pour l'activer.

##### Sous windows:

`python -m venv env`

pour la création de l'environnement, puis:

`env\Scripts\activate.bat`

pour l'activer.

#### Instalation des dépendances
Il ne reste plus qu'à utiliser la commande suivante:

`pip install -r requirements.txt`


Et voilà, vous pouvez maintenant lancer le script grâce à la commande qui suit:
##### Sous linux et mac:

`python3 Controleur.py`


##### Sous windows:

`python Controleur.py`


#### Vérification de conformité avec Flake8:
Afin de générer un nouveau rapport flake8 en HTML qui vérifie la conformiter PEP 8 avec l'option de longueur de ligne fixée à 119, il suffit, apres avoir activé l'environement virtuel, d'utiliser la commande qui suit dans le terminal:

`flake8 --format=html --htmldir=flake8-rapport`

le rapport sera allors disponible dans le repertoir source du programe, dans le dossier "flake8-rapport".


## Fonctionnement:
Une fois l'instalation effectuée et le programme exécuté, il permet de créer un, ou plusieurs, nouveaux tournois et d'ajouter de nouveaux joueur à la base de données générale.
Les joueur peuvent ensuite, via leur numéro INE, être ajoutés diréctement à un tournoi précédemment créé. Les tournois sont créés avec un nombre de rounds par défaut de 4. Ce nombre est modifiable lors la création du tournoi.
En cas de nombre de participants impair, le programme décidera aléatoirement à chaque round quel joueur ne participera pas aux matchs.

### Lancement ou reprise d’un tournoi:
Une fois le tournoi créé et les participants ajoutés, il suffit de choisir dans la liste le tournoi désiré afin de le commencer. Les matchs du premier round seront alors affichés à l’écran.
Une fois tous les matchs de ce round terminés, la suite du programme nécessite de désigner les gagnants des différents matchs via une saisit au clavier.
Une fois cela fait, un résumé du round s’affiche alors a l’écran.
À cet instant, et à chaque fois qu’un round est terminé, l’utilisateur aura le choix entre arrêter le tournoi et le reprendre plus tard, ou le continuer.
Pour reprendre un tournoi qui a été précédemment arrété, il suffit de lancer l’application, de choisir « Lancer / reprendre le tournoi » et de sélectionner le tournoi désiré.

### Affichage du résumé:
Il est possible d’afficher la liste complète des joueurs ainsi que des données des différents tournois, non commencés comme déjà finis. Pour ce faire, il suffit de choisir l’option dans le menu du programme.


