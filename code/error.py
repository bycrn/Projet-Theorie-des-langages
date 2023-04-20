
# test script 1
def error_number_element(script_liste) :
    if len(script_liste) == 0 :
        raise ValueError("There are no transitions defined")

    set1 =  set([len(script_liste[i]) for i in range(0,len(script_liste), 2)])
    if len(set1) != 1:
        raise ValueError("Incorrect number of elements in reading lines")

# test script 2
def error_script_syntax(script_liste) :
    NBR_TAPES = len(script_liste[0]) - 1

    if script_liste[0][0] != "I" :
        raise ValueError("initial state in 1st line should be 'I'!")

    # # wrinting lines syntax check (writing elements & move symbols)
    for i in range(1, len(script_liste) - 1, 2):
        for m in range(len(script_liste[0]), len(script_liste[1])):
            if script_liste[i][m] != "<" and script_liste[i][m] != ">" and script_liste[i][m] != "-":
                right_syntax_symbol()
                raise ValueError(f"Incorrect movements symbol in line {i}")

# test script 3
# Check if a transition already exists
def check_transition(script_liste):
    for i in range(0, len(script_liste), 2):
        for j in range(i+2, len(script_liste), 2):
            if script_liste[i] == script_liste[j]:
                raise ValueError(f"Transition {script_liste[i]} in line {j} is already defined")

def right_syntax_symbol():
    print("! Correct syntax ! Movements must be\nStay :  - \nMove right : > \nMove left : <")



def manage_script_error(script_liste):
    error_number_element(script_liste)
    error_script_syntax(script_liste)
    check_transition(script_liste)


# error no tansition
def error_transition_lecture(liste):
    if len(liste) == 0:
        raise ValueError("!Failed initialization or update of current state and head_position!")


# # reading lines syntax check
    # for i in range(0,len(script_liste), 2):
    #     for j in range(1,len(script_liste[i])):
    #         if script_liste[i][j] != "0" and script_liste[i][j] != "1" and script_liste[i][j] != "_":
    #             right_alphabet()
    #             raise ValueError(f"Incorrect reading elements in line {i}")
    
    # # wrinting lines syntax check (writing elements & move symbols)
    # for i in range(1, len(script_liste) - 1, 2):
    #     for j in range(1, NBR_TAPES):
    #         if script_liste[i][j] != "0" and script_liste[i][j] != "1" and script_liste[i][j] != "_":
    #             right_alphabet()
    #             raise ValueError(f"Incorrect elements for writing in line {i}")