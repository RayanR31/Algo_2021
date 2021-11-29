def tri_insertion(tab): 
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
tab = [4524, 554, 425, 4233, 3532, 2, 65333, 7530]
tri_insertion(tab) 
for i in range(len(tab)): 
    print ("% d" % tab[i])