from error import manage_script_error

def reading_script(name):
    match name:

        case "LEFT":
            path = "description_mt/LEFT.txt"

        case "COPY":
            path = "description_mt/COPY.txt"

        case "ERASE":
            path = "description_mt/ERASE.txt"

        case "SEARCH":
            path = "description_mt/SEARCH.txt"

        case "ADDYTOZ":
            path = "description_mt/binaryaddition.txt"
        
        case "one":
            path = "description_mt/onetape.txt"
                
        case "two":
            path = "description_mt/twotapes.txt"

        case "test":
            path = "description_mt/testsix.txt"

        case "t2":
            path = "description_mt/test2.txt"
        
        case "add":
            path = "description_mt/binaryaddition.txt"

        case "mult":
            path = "description_mt/binarymultiplication.txt"

        case "sort":
            path = "description_mt/sortbinary.txt"

        case other :
            raise ValueError('could not find the file')

    with open(path, 'r') as f:
        lines = f.readlines()
        l = [line.replace("\n","").split(",") for line in lines 
                            if not line.startswith("//") and line.strip()]

    # manage_script_error(l)

    return l



def link_copy(m1):
    ind = []
    compteur = 0
    # initializing m2 
    for i in range(len(m1)):
        if "COPY" in m1[i]:
            ind.append(i)
    
    for k in range(len(ind)) :
        m2 = reading_script("COPY")
        for kk in range(len(m2)):
            m2[kk][0] = m2[kk][0] + str(k)
        index = ind[k] + compteur
        tape_i = int(m1[index][1])
        tape_j = int(m1[index][2])
        m2[-1][0] = m1[index][-1]
        mi = min(tape_i,tape_j)
        ma = max(tape_i,tape_j)

        # exchange tapes in copy if i > j 
        if tape_i > tape_j:
            for i in range(0,len(m2),2):
                el_i = m2[i].pop(-1)
                el_j = m2[i].pop(-1)
                m2[i].extend([el_i, el_j])
                symb_i = m2[i+1].pop(-1)
                symb_j = m2[i+1].pop(-1)
                el_i = m2[i+1].pop(-1)
                el_j = m2[i+1].pop(-1)
                m2[i+1].extend([el_i, el_j, symb_i, symb_j])
                    
        # insert in m2 supplementary tapes between states and min(i,j)
        if mi > 1 :
            for i in range(1,len(m2),2):
                for j in range(1,mi):
                    m2[i-1].insert(j, m1[index-1][j])
                    m2[i].insert(j, m1[index-1][j])
                    m2[i].insert(j+3, '-')

        
        if  abs(tape_j - tape_i) > 1 :
            for i in range(1,len(m2),2):
                for j in range(mi+1 , ma):
                    m2[i-1].insert(j, m1[index-1][j])
                    m2[i].insert(j, m1[index-1][j])
                    m2[i].insert(j+4, '-')

        
        # insert in m2 supplementary tapes after max(i,j)
        if ma < len(m1[index-1]):
            for i in range(1,len(m2),2):
                for j in range(ma+1, len(m1[index-1])):
                    m2[i-1].insert(j, m1[index-1][j])
                    m2[i].insert(j, m1[index-1][j])
                    m2[i].insert(j+5, '-')


        # change the called machine in the transition by the transition in m2
        for j in range(0,6,2):
            if m1[index-1][1:] == m2[j][1:]:
                m1[index] = m2[j+1]
        
        # finally add all the transition in m1
        ii = 1
        for el in m2:
            m1.insert(index+ii, el)
            ii += 1
            compteur +=1
    
    return m1

def link_search(m1):
    ind = []
    compteur = 0
    # initializing m2 
    for i in range(len(m1)):
        if "SEARCH" in m1[i]:
            ind.append(i)

    # initializing m2  
    for k in range(0,len(ind)) :
        m2 = reading_script("SEARCH")
        for kk in range(len(m2)):
            m2[kk][0] = m2[kk][0] + str(k)
        index = ind[k]+compteur
        nbr = int(m1[index][1])
        m2[-1][0] = m1[index][-1]
        a = m1[index][2]

        for i in range(len(m2)):
            if m2[i][1] == "a":
                m2[i][1] = a
            if m2[i][1] == "b":
                if a == "0":
                    m2[i][1] = "1"
                else :
                    m2[i][1] = "0"
            if m2[i][1] == "c":
                if a == "1":
                    m2[i][1] = "0"
                else :
                    m2[i][1] = "#"

        # insert in m2 supplementary tapes before tape i
        for i in range(1,len(m2),2):
            for j in range(1,nbr):
                m2[i-1].insert(j, m1[index-1][j])
                m2[i].insert(j, m1[index-1][j])
                m2[i].insert(j+2, '-')

        # insert in m2 supplementary tapes after i
        if nbr <  len(m1[index-1]):
            for i in range(1,len(m2),2):
                for j in range(nbr + 1, len(m1[index-1])):
                    m2[i-1].insert(j, m1[index-1][j])
                    m2[i].insert(j, m1[index-1][j])
                    m2[i].insert(j+3, '-')

        # change the called machine in the transition by the transition in m2
        for j in range(0,8,2):
            if m1[index-1][1:] == m2[j][1:]:
                m1[index] = m2[j+1]

        # finally add all the transition in m1
        ii = 1
        for el in m2:
            m1.insert(index+ii, el)
            ii += 1
            compteur +=1

    return m1


def link_single_tape(m1,called):
    ind = []
    compteur = 0
    # initializing m2 
    for i in range(len(m1)):
        if called in m1[i]:
            ind.append(i)
    
    # initializing m2  
    for k in range(0,len(ind)) :
        m2 = reading_script(called)
        for kk in range(len(m2)):
            m2[kk][0] = m2[kk][0] + str(k)
        index = ind[k] + compteur
        nbr = int(m1[index][1])
        m2[-1][0] = m1[index][-1]

        # insert in m2 supplementary tapes before tape i
        for i in range(1,len(m2),2):
            for j in range(1,nbr):
                m2[i-1].insert(j, m1[index-1][j])
                m2[i].insert(j, m1[index-1][j])
                m2[i].insert(j+2, '-')

        # insert in m2 supplementary tapes after i
        if nbr <  len(m1[index-1]):
            for i in range(1,len(m2),2):
                for j in range(nbr + 1, len(m1[index-1])):
                    m2[i-1].insert(j, m1[index-1][j])
                    m2[i].insert(j, m1[index-1][j])
                    m2[i].insert(j+3, '-')

        # change the called machine in the transition by the transition in m2
        if called == "LEFT" or called == "ADDYTOZ":
            temp = 6
        if called == "ERASE":
            temp = 8
            
        for j in range(0,temp,2):
            if m1[index-1][1:] == m2[j][1:]:
                m1[index] = m2[j+1]
                done = True
            else :
                done = False

        if not done :
            le = len(m2[0])
            liste1 =  [m2[1][0]]
            liste1.extend(m1[index-1][1:])
            liste1.extend(m2[1][le:])
            m1[index] = liste1

        # finally add all the transition in m1
        ii = 1
        for el in m2:
            m1.insert(index+ii, el)
            ii += 1
            compteur +=1

    for el in m1:
        print(el)

    return m1


def final_script(name):
    m1 = reading_script(name)
    for el in m1:
        if "LEFT" in el:
            m1 = link_single_tape(m1, "LEFT")
        if "ERASE" in el:
            m1 = link_single_tape(m1, "ERASE")
        if "SEARCH" in el:
            m1 = link_search(m1)
        if "COPY" in el:
            m1 = link_copy(m1) 
        if "ADDYTOZ" in el:
            m1 =link_single_tape(m1, "ADDYTOZ")
         

    return m1
