"""
@author: Maxime Fagnan
@email: maxime.fagnan@brebeuf.qc.ca

-Commentaires � nettoyer
-Utilisation de la matrice transposee possible pour reduire la repetition
"""

#------------ def Fonctions ------------

#Trouve le meilleur candidat à partir de (row,col) en regardant par en bas
def findBelow(row,col):
    limD=n
    limG=-1
    sol_max=n-row
    #Trier les arbres par rang�e, puis par colonne
    s_trees=sorted(trees,key=lambda t:(t[0],t[1]))
    #r�duire la solution possible � chaque fois que l'on rencontre un arbre
    for t in s_trees:
        r=t[0]
        c=t[1]
        if(r>=row): #ne pas prendre en compte les arbres plus hauts que row
            d_Ver=r-row+1 #distance verticale de row � l'arbre (inclusif)
            #Ajout de l'arbre aux contraintes
            if(c>=col): limD=min(limD,c)
            if(c<=col): limG=max(limG,c)
            d_Hor= limD-limG-1 #distance entre les arbres jusqu'� t
            #ajustement de la solution maximale:
            if(d_Ver>sol_max):
                #Prochain arbre trop loin pour les contraintes d�j� trouv�es
                return sol_max 
            if(d_Ver>d_Hor):
                #Arbre r�duit trop la dist horizontale pour que la dist_verticale soit inclusive
                return d_Ver-1 
            elif(d_Ver<=d_Hor):
                #Arbre r�duit la solution maximale, mais continuons d'explorer
                sol_max=min(d_Hor,sol_max) 
    return sol_max

#Trouve le meilleur candidat � partir de (row,col) en regardant par la droite
def findRight(row,col):
    limB=n
    limH=-1
    sol_max=n-col
    #Trier les arbres par colonne, puis par rang�e
    s_trees=sorted(trees,key=lambda t:(t[1],t[0]))
    #r�duire la solution possible � chaque fois que l'on rencontre un arbre
    for t in s_trees:
        r=t[0]
        c=t[1]
        if(c>=col):
            d_Hor=c-col+1 #distance horizontale incluant l'arbre
            #R�ajuster la solution maximale par rapport � la distance entre les arbres
            if(r>=row): limB=min(limB,r)
            if(r<=row): limH=max(limH,r)
            d_Ver= limB-limH-1 #entre les arbres
            #ajuster la solution
            if(d_Hor>sol_max):
                return sol_max #Prochain arbre trop loin pour les contraintes d�j� trouv�es
            if(d_Hor>d_Ver):
                return d_Hor-1 #Prochain arbre r�duit trop la dist verticale
            elif(d_Hor<=d_Ver):
                sol_max=min(d_Ver,sol_max) #ne pas retourner car le prochain arbre pourrait �tre sur la m�me colonne et r�duir sol_max
    return sol_max


#------------ debut ------------

#traitement des données
n=int(input()) #Matrice de n à 0
t=int(input()) #Nombre d'arbres
trees=[] #Liste contenant tous les arbres
while(t>0):
    s=input().split()
    coord=list(map(int,s))
    coord[0]-=1
    coord[1]-=1
    trees.append(coord)
    t=t-1


sorted(trees,key=lambda t:(t[0],t[1]))

#Solution initiale (commencer a�partir d'en haut)
sol=max(findBelow(0, 0),0)

#Trouver les solutions en dessous de chaque arbre
for t in trees:
    row=t[0]
    col=t[1]
    temp=[sol]
    if(row!=n-1):
        temp.append(findBelow(row+1,col))
    if (col!=n-1):
        temp.append(findRight(row,col+1))
    sol=max(temp)
print(sol)