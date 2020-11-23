import random
from datetime import datetime
random.seed(datetime.now())
import time
import numpy as np
import matplotlib.pyplot as plt
fichiers=[]
for num in range(10):
    nomFichier = "path\\to\\file\\gen{}.txt".format(num+1)
    fichiers.append(open(nomFichier, "a+"))


totaux = np.zeros((10,4)) #10 elements
pourcentages = np.zeros(10)

numEssais = 1000000
popInitiale = 50

for p in range(numEssais):
    population = []
    popActuelle = 50
    genepool = [
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
            2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]
    decomptes= np.zeros((10,4)) #10 elements
    for i in range(10):
        decompte = np.array([0,0,0,0]) #4elements
        numHomoRec=0
        numHetero=0
        numHomoDom=0
        decompte[3]=popActuelle
        for j in range(popActuelle):
            one = random.choice(genepool)
            genepool.remove(one)
            two = random.choice(genepool)
            genepool.remove(two)
            if((one == 1) and (two == 1)):
                popActuelle -= 1
                decompte[0] +=1
            elif(((one == 1)and(two == 2))or((one == 2)and(two == 1))):
                genepool.append(two)
                genepool.append(one)
                decompte[1] +=1
            else:
                genepool.append(two)
                genepool.append(one)
                decompte[2] +=1
        decomptes[i] = np.add(decomptes[i], decompte)
        fichiers[i].write("{},{},{},{},{}\n".format(p+1,decompte[0], decompte[1], decompte[2], decompte[3]))
    totaux = np.add(totaux, decomptes)
    

for fichier in fichiers:
    fichier.close()

