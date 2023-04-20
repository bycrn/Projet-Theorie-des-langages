from script_MT import final_script

script_liste = []
# K number of tapes
K = 0

class MachineTuring:
    def __init__(self):
        self.current_state = "I"
        self.head_position = []
        self.tapes = {}
        self.script = []
        self.create_machine()
    
    def create_machine(self):
        name = input("Wich turing machine do you wish to use : ")
        script_liste = final_script(name)
        self.script = script_liste
        # affichage de la description de la machine de Turing
        print("description de la machine : ")
        for el in script_liste:
            print(el)
        K = len(script_liste[0]) - 1
        #init tapes
        self.tapes = {i : ["$"] for i in range(0, K)}
        #init head position of mt in the tapes
        self.head_position = [1 for i in range(0, K)]
        self.head_position[0] = 1
    
    def init_tape(self, word):
        for c in word:
            self.tapes[0].append(c)
        if len(self.tapes) > 1 :
            for i in range(1, len(self.tapes)):
                self.tapes[i].append("_")

    # str

    def get_tapes(self) :
        for i in range(len(self.tapes)):
            print(f"{self.tapes[i]}")

    def str_step_mt(self) :
        print("bandes = ")
        for value, head in zip(self.tapes.values(), self.head_position):
            print(value)
            print(head)
        print("new state", self.current_state)
        print("\n")


    # getter 

    def get_currrent_state(self) :
        return self.current_state

    #change index to tape_nbr - 1 
    def get_headposition(self, tape_nbr):
        return self.head_position[tape_nbr]
    
    def get_transition(self):
        transition_lecture = [self.get_currrent_state()]
        for i in range(len(self.tapes)):
            index = self.head_position[i]
            if self.tapes[i][index] == "$":
                transition_lecture.append("_")
            else :
                transition_lecture.append(self.tapes[i][index])
        return transition_lecture

    # setter

    def set_current_state(self,new_state):
        self.current_state = new_state


    def stop_machine(self):  
        transition = self.get_transition()
        if self.get_currrent_state() == "F":
            print("ACCEPTED")
            return False
            
        elif transition not in self.script :
            print("WORD REJECTED")
            return False

        else :
            return True


    def one_step(self) :
        # démarrage 
        #lecture dans les bandes de la machine et récuppération de la lecture 
        # dans une liste
        transition_lecture = self.get_transition()
        K = len(self.script[0]) - 1  

        #lecture et écriture dans les tapes
        for i in range(0, len(self.script), 2):
            if  transition_lecture == self.script[i]:
                print("\ncurrent state : ", self.current_state)
                # change state
                self.set_current_state(self.script[i+1][0])
                # writing in tapes 
                for w in range(0, len(self.tapes)):
                    pos_write = self.head_position[w]
                    j = w + 1
                    self.tapes[w][pos_write] = self.script[i+1][j]

                # change head position and move
                moves = [self.script[i+1][m] for m in range(1 + K, len(self.script[i+1]))]
                for _ in range(len(moves)):
                    if moves[_] == "<": 
                        if self.head_position[_] == 0 :
                            self.head_position[_] = 1
                            self.tapes[_].insert(0, "_")
                        if self.head_position[_] > 0 : 
                            self.head_position[_] -= 1

                    elif moves[_] == ">": 
                        self.head_position[_] += 1
                        if len(self.tapes[_]) <= self.head_position[_]:
                            self.tapes[_].append("_")

                    elif moves[_] == "-": 
                        pass

        self.str_step_mt()
        

    
        


    
