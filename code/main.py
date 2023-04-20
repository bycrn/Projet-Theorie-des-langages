# machine de turing
from MT import MachineTuring
from logo import logo
from script_MT import reading_script

print(logo + "\n Projet de Theorie des langages")

def machine_simulation(self):
    on = True
    while on :
        self.one_step()  
        on = self.stop_machine()

# fonction qui initialise une instance de la structure MT à 
# partir d’un mot d’entrée et d’un fichier contenant une 
# description d’une machine de Turing

def question_1(self):
    word = input("Insert a word: : ").lower()
    """création de la machine""" 
    # initaialisation de la machine à partir du mot d'entrée
    self.init_tape(word)
    # affichage des bandes 
    print("tapes : ")
    self.get_tapes()
    

# Ecrire une fonction qui étant donnée une machine de Turing, 
# lui fait exécuter un pas de calcul.

def question_2(self):
    question_1(self)
    self.one_step()
    self.str_step_mt()

# Ecrire une fonction qui prend comme argument un mot et une machine 
# de Turing et qui simule le calcul de la machine sur le mot jusqu’à
# atteindre l’état final. Bravo, vous avez réalisé une machine
# universelle.

def question_3(self):
    question_1(self)
    machine_simulation(self)

# Donner le code des machines de Turing suivantes, chacun dans un fichier distinct

def question_5():
    print("\nPositionner la tête de lecture sur la lettre la plus\nà gauche de la bande numèro i : LEFT,i")
    left = reading_script("LEFT")
    for el in left:
        print(el)
    print("\nEffacer la bande numèro i : ERASE,i")
    erase = reading_script("ERASE")
    for el in erase:
        print(el)
    print("\nCopier la bande i sur la bande j : COPY,i,j")
    copy = reading_script("COPY")
    for el in copy:
        print(el)
    print("\nPositionner la tête de lecture sur le premier caractère a ∈ Σ\nsur la bande i : SEARCH,i,a")
    search = reading_script("SEARCH")
    for el in search:
        print(el)


working = True
while working:
    print("Reminder : Σ = {0,1}")
    choice = input("\nChoisissez une question : ")
    

    match choice :
        case "1":
            machine = MachineTuring()
            question_1(machine)
            
        case "2":
            machine = MachineTuring()
            question_2(machine)
        
        case "3":
            machine = MachineTuring()
            question_3(machine)
        
        case "5":
            question_5()

        case "7" | "8":
            print("use sort or mult")
            self = MachineTuring()
            question_3(self)

        case other:
            print("Choose another question")


    still_going = input("Want to continue ? y/n : \n").lower()
    if still_going == "y" :
        working = True
    elif still_going == "n" :
        working = False
        print("Bye Bye")
    else :
        print("incorrect input\n ")
        still_going = input("incorrect input\nWant to continue ? y/n : \n").lower() 






