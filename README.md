# plan2fab README

L'objectif de est permettre la documentation de projet de réalisation dans un fablab. Dans un premier temps dans le contexte de l'ÉcoDesignFablab de Mozinor à Montreuil.

## Development

Utilisation de VirtualEnv (apparement, pyramid l'encourage... faire autrement ?)

Dans le cas d'un premier usage il faut créer un repertoire pour stocker les executables utilisé par VirtualEnv et Python.

```bash
virtualenv plan2fab_devenv && cd plan2fab_devenv && source bin/activate
```

Une fois ce repertoire mis en place, et une fois dedans, nous pouvons faire les éléments habituel:

```bash
git clone https://github.com/apedec/plan2fab.git && cd plan2fab
```

On accède ensuite au commande habituel:

```bash
python setup.py develop
initialize_plan2fab_db development.ini
pserve development.ini
```

