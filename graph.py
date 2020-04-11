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

def makePolice(G, n, day):

    l = [[] for _ in range(n)]

    for i in range(n):
        for j in range(day):
            d = random.randint(0,len(G)-1)
            a = random.choice(G[str(d)])
            l[i].extend([d,a])
    return l

def polisteToText(l, nbSup,nbSupJour):
    s = str(len(l)) + "\n" + str(nbSupJour)
    for i in range(len(l)):
        s += "\n"
        for j in range(len(l[i])):
            s += str(l[i][j]) + " "
    return s



def genererNiveau(nbVilles=100,ratioElag=0.7,ratioPolice=0.7,fichier="resultat.txt"):

    # GRAPH
    nbSuppressions = int(ratioElag*nbVilles)
    G = makeComplete(nbVilles)
    # suppression des arcs
    removeNarcs(G,nbSuppressions)
    # creation de la liste
    l = graphToList(G)
    # creation de la version texte
    s = listToText(l)

    ## POLICE
    nbJours = nbVilles +1
    nbSuppressionsJour = int(ratioPolice*nbJours)
    # créer la liste des jours
    l2 = makePolice(G, nbJours, nbSuppressionsJour)
    s2 = polisteToText(l2,nbJours, nbSuppressionsJour)


    # enregistrer dans un fichier texte
    f = open(fichier,"w")
    f.write(s+s2)
    f.close()