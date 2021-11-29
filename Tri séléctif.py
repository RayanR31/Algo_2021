def tri_selection(tab):
   for i in range(len(tab)):
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab
tab = [5, 45, 89, 332, 414, 752, 4214, 42]
 
tri_selection(tab)
 
for i in range(len(tab)):
    print ("%d" %tab[i])