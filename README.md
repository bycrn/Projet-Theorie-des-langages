
# Projet – Simulation de Machines de Turing

## **Description** 

    L’implantation en Python d’une simulation de l’exécution pas à pas d’une machine de Turing avec linker sans interface.

### **DM** - Simulation de l’exécution d’une machine de Turing

Coder uniquement en Python (POO) sans GUI.

Des fichiers textes ont été utilisés pour décrire les machines de Turing.

Création de fonction linker pour appeler d'autres machines (ss formes de fichiers txt).



## Simulation de l'exécution d'une machine de Turing


### 1. Les stuctures de données utilisées 

Les structures de données utilisées dans ce projet sont : 

- Une classe 
- dictionnaire pour stocker les bandes.
- liste : bande


### 2. Configuration 

Initialisation de l'état courant, l'état des bandes et la position des têtes de lecture avec la fonction :

    create_machine()

### 3. Méthode qui exécute la machine de Turing d'un pas de calcul puis jusqu'à final state

    one_step()

La machine universelle est ensuite créer  dans le *main.py* en prenant un mot en argument et en simulant le calcul de la machine sur le mot jusqu’à atteindre l’état final.

### 4. Code des Machines 

Appel de Machine de Turing, qu'on définit par une transition.

Les machines appelées sont stockées dans le dossier *description_mt*.

`LEFT*i*` : Se placer sur la lettre la plus à gauche de la bande numéro i 

`RIGHT*i*` : Se placer sur la lettre la plus à droite de la bande numéro i

`SEARCH*i,a*` : Se positionner sur le premier caractère a ∈ Σ sur la bande i

`ERASE*i*` : Effacer la bande numéro i

`COPY*i,j*` : Copier la bande i sur la bande j


## Machine qui appelle

Une machine M a la transition spéciale **(q, a, M, q′)**, alors dans l’état q et à la lecture de a elle lance le calcul de la machine M′. Quand M′ a fini
son calcul, alors M passe dans l’état q′.

On a en entrée le code de deux machines de Turing M1 et M2 tel que la machine M1 fait des appels à M2. Votre fonction doit produire une machine M3, sans appel à M2 qui réalise le même calcul que M1.

- **Dans script_MT**

Création d'une fonction `final_script(name)` qui détecte les machines appellantes et insert le code des m2 dans m1.

`final_script(name)` appelle les fonctions :

Pour LEFT et ERASE :

    link_single_tape(m1,called)

Pour SEARCH :

    link_search(m1)

Pour COPY :

    link_copy(m1)


`final_script(name)` retourne une nouvelle machine m3.

## Machine plus compliquée

Création de deux machines de Turing :

### 1ère Machine

Multiplier deux nombres en binaire x et y en utilisant la méthode égyptienne.
On initalise z (le résultat) à 0 et tant que x est supérieur strict à 0 on fait :
- si x est pair, ` x = x/2 ` et ` y = y ∗ 2 `
- si x est impair, ` x = x/2`, ` z = z + y` et ` y = y ∗ 2`
Vous devrez appeler la machine r´ealisant une addition

    binaryaddition.txt

    binnarymultiplication.txt


### 2ème Machine

Etant donnée une entrée de la forme ` 01#00#11#00#10` qui représente un tableau avec un nombre quelconque d’entiers sur deux bits, donner une machine de Turing qui trie ce tableau.

    sortbinary.txt
## 🛠 Skills
Python 🐍

