# plan2fab README

L'objectif de est permettre la documentation de projet de réalisation dans un fablab. Dans un premier temps dans le contexte de l'ÉcoDesignFablab de Mozinor à Montreuil.

## Développement

On récupère d'abord les sources avec git :

```bash
git clone https://github.com/apedec/plan2fab.git
cd plan2fab
```

On crée un virtualenv (environnement virtuel Python) dans lequel on va installer le projet et ses dépendances :

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt -r dev-requirements.txt
python setup.py develop
```

On crée un utilisateur et une base de données dans Postgres. Par exemple, sous Ubuntu Linux :

```bash
sudo apt-get install postgresql
sudo su - postgres -c "createuser apedec && createdb plan2fab --owner=apedec"
```

On initialise la base de données :

```bash
initialize_plan2fab_db development.ini
```

On lance le serveur web de développement :

```bash
pserve development.ini
```
