import random

def makeComplete(nbSommet):

    G = {}

    for i in range(nbSommet):

        G[str(i)] = []
        for j in range(nbSommet):
            if i!=j:
                G[str(i)].append(j)
    return G


def isConnex(G):

    visited = [False] * len(G)
    currentNode = G['0']
    visited[0] = True

    for indNodes in currentNode:
        if not visited[indNodes]:
            parcours(G,indNodes,visited)
    
    U = filter(lambda x:x==False,G)
    return len(U)==0


def parcours(G,ind,visited):
    visited[ind] = True
    
    for indices in G[str(ind)]:
        if not visited[indices]:
            parcours(G,indices,visited)


def removeConnexion(G):
    ind = str(random.randint(0,len(G)-1))
    ind2 = random.choice(G[ind])

    i = G[ind].index(ind2)
    del G[ind][i]
    j = G[str(ind2)].index(int(ind))
    del G[str(ind2)][j]

    # si c'est connexe on return true
    if isConnex(G):
        return True
    
    # sinon on remet l'arrete et on return false
    G[ind].append(ind2)
    G[str(ind2)].append(ind)
    return False

def removeNarcs(G,n):
    for _ in range(n):
        a = removeConnexion(G)
        while a == False:
            a = removeConnexion(G)
        
def graphToList(G):
    l = [[] for _ in range(len(G))]
    for key,value in G.items():
        l[int(key)] = value
    return l


def listToText(l):
    s = str(len(l))+"\n"
    for i in range(len(l)):
        s += str(len(l[i]))
        for j in range(len(l[i])):
            s += " "
            s += str(l[i][j])
        s += "\n"
    return s

###### MAIN

# parametres
nbVilles = 100
nbSuppressions = (nbVilles/100*30)

# creation du graph
G = makeComplete(nbVilles)

# suppression des arcs
removeNarcs(G,nbSuppressions)

# creation de la liste
l = graphToList(G)

# creation de la version texte
s = listToText(l)

# enregistrer dans un fichier texte
f = open("resultat.txt","w")
f.write(s)
f.close()

