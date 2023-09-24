import numpy as np

m = int(input("Nombre de lignes : "))
n = int(input("Nombre de colonnes : "))

a = np.zeros((m,n))

for lin in range(1,m+1):
    for col in range(1,n+1):
        coeff = input("Coeff  "+str(lin)+","+str(col)+"  : ")
        a[lin-1, col-1] = coeff

print(a)



linDernierPivot = -1

for col in range(0,n):

    # Recherche du coefficient le plus grand de la colonne j
    maxi = a[linDernierPivot + 1, col]
    k = linDernierPivot + 1
    for lin in range(linDernierPivot + 1,m):
        if a[lin, col] > maxi:
            maxi = a[lin, col]
            k = lin # Correspond à l'indice de la ligne du coeff max

    # Si le max est 0, on ne fait rien et on passe à la ligne suivante sinon on fait quelques opérations
    if maxi != 0:
        if linDernierPivot + 2 < m:
            linDernierPivot = linDernierPivot + 1

        # On divise la ligne du pivot par la valeur du pivot pour avoir un pivot qui vaut 1
        for y in range(0,n): # On parcourt les colonnes
            a[k, y] = a[k, y] / maxi

        # On met la ligne contenant le pivot où le pivot est censé être (s'il n'est pas sur la bonne ligne)
        if k != linDernierPivot:
            tmp = []
            for y in range(0,n): # On parcourt les colonnes
                tmp.append(a[linDernierPivot, y]) # Stockage des valeurs de la ligne 'linDernierPivot'
                a[linDernierPivot, y] = a[k, y] # Remplacement de la ligne 'linDernierPivot' par la ligne k
                a[k, y] = tmp[y] # Remplacement de la ligne k par la linge 'linDernierPivot'


        # Pour toutes les lignes (sauf la ligne contenant le pivot), on soustrait le bon
        # nombre de fois la ligne contenant le pivot pour faire apparaitre que des 0 sous
        # et sur le pivot
        for x in range(0,m): # On parcourt les lignes
            if x != linDernierPivot:
                constante = a[x, col]
                for y in range(0,n): # On parcourt les colonnes
                    a[x, y] = a[x, y] - a[linDernierPivot, y] * constante
    


print(a)

'''
r = 0                                       (r est l'indice de ligne du dernier pivot trouvé)
     Pour j de 1 jusqu'à m                       (j décrit tous les indices de colonnes)
     |   Rechercher max(|A[i,j]|, r+1 ≤ i ≤ n). Noter k l'indice de ligne du maximum
     |                                           (A[k,j] est le pivot)
     |   Si A[k,j]≠0 alors                       (A[k,j] désigne la valeur de la ligne k et de la colonne j)
     |   |   r=r+1                               (r désigne l'indice de la future ligne servant de pivot)
     |   |   Diviser la ligne k par A[k,j]       (On normalise la ligne de pivot de façon que le pivot prenne la valeur 1)
     |   |   Si k≠r alors
     |   |       |   Échanger les lignes k et r  (On place la ligne du pivot en position r)

     |   |   Pour i de 1 jusqu'à n               (On simplifie les autres lignes)
     |   |   |   Si i≠r alors
     |   |   |   |   Soustraire à la ligne i la ligne r multipliée par A[i,j] (de façon à annuler A[i,j])
'''