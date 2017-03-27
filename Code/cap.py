import math
import copy
from matplotlib import pyplot as plt

#Fabriquation du dictionnaire des villes
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
carte = dict()
for ligne in liste_lignes:
    liste_de_mots = ligne.strip().split(",")
    Nom,Rev,nbHab,Rsurface,McDo,Quick,echecM,echecQ,Qtm1,R = liste_de_mots
    R = float(nbHab)*0.003*float(Rev)/12
    carte[Nom] = {"rev":int(Rev),"nbHab":int(nbHab),"Rsurface":float(Rsurface),"McDo":int(McDo),"Quick":int(Quick),"echecM":int(echecM),"echecQ":int(echecQ),"R":float(R),"Qtm1":int(Qtm1)}

fichier.close()
print(carte["Paris16"]["R"]/8)
#Donnees
pVK = 8
pVM = 8
taxe = 0.6
moisAm = 24
moisnul = 10000
w = 0.3
coutMenu = 5
coutEntretien = 30000
coutImplantation = 800000
CompteM = 800000
CompteQ = 800000
impotprofit = 0.67
impotsiege = 0.93

#CLASSES

class Siege:
    def __init__(self,marque,pv,dicProfit,dicScore,epargne,pref):
        self.marque = marque
        self.pv = pv
        self.dicProfit = dicProfit
        self.dicScore = dicScore
        self.epargne = epargne
        self.echec = "echec" + marque[0]
        self.newResto = set()
        self.mois = 0
        self.profit = 0
        self.pref = pref
        self.nbR = 0

    def recolte(self):
        """Recolte les profits"""
        biff = 0
        for ville in self.dicProfit:
            biff += self.dicProfit[ville]
        self.profit = biff
        self.epargne = self.epargne+ biff*impotprofit

    def desimp(self):
        """Desimplante et ajoute des malus si necesaire"""
        for ville in self.dicProfit:
            if carte[ville][self.marque] != 0 and dicProfit[ville]/carte[ville][self.marque]<moisnul :
                carte[ville][self.echec] += 1
            if carte[ville][self.echec] >= 12:
                carte[ville][self.marque] -= 1
                carte[ville][self.echec] = 0

    def choixNewResto(self):
        """Renvoie l'ensemble des emplacements qui recevront un restaurant"""
        dicEmplCool = EmplCool(self.dicScore)
        self.newResto = set()
        nbMax = self.epargne // coutImplantation
        if nbMax > len(dicEmplCool):
            return changeenset(dicEmplCool)
        e = 0
        fort = 0
        best = ""
        while e < nbMax:
            for ville in dicEmplCool:
                if not(ville in self.newResto):
                    if dicEmplCool[ville]>fort:
                            fort=dicEmplCool[ville]
                            best=ville
            self.newResto.add(best)
            e+=1
            fort = 0
            best = ""

    def imp(self):
        """Implante les nouveaux restaurants"""
        for ville in self.newResto:
            carte[ville][self.marque] += 1
            self.nbR += 1
        self.epargne -= len(self.newResto)*coutImplantation

    def maj(self,nomEl,newEl):
        if nomEl == "Profits":
            self.dicProfit = newEl
        elif nomEl == "Scores":
            self.dicScore = newEl
            
    def impots(self):
# ca ns parait etre du caca: taux dimposition trop faible (#palier d'imposition propre à chaque profit d'un resto <3)
        self.epargne = self.epargne*impotsiege

#Creation des Sieges
dic = dict()
for ville in carte:
    dic[ville] = 0

McDo = Siege("McDo",pVM,dic,dic,CompteM,0.99)
Quick = Siege("Quick",pVK,dic,dic,CompteQ,0.98)

#FONCTIONS
def EmplCool(dicScore):
    """Renvoie la liste des villes dans lesquelles recevoir un restaurant serait avantageux"""
    dicEmplCool = dict()
    for ville in dicScore:
        if dicScore[ville] * moisAm >= coutImplantation:
            dicEmplCool[ville] = dicScore[ville]
    return dicEmplCool

def unouzero(n):
    if n == 0:
        return 0
    return 1

def changeenset(dic):
    se = set()
    for a in dic:
        se.add(a)
    return se

def fonctionDemande(carte,ville):
    """Retourne la Qte de consommations de menus Quick et McDo en fonction des infos sur la ville"""
    dicVille = copy.deepcopy(carte[ville])
    Nm = dicVille["McDo"] #Nombre de McDo dans la ville
    Nk = dicVille["Quick"] # ref Quick
    S = dicVille["Rsurface"] #Qui est la racine carree de la surface
    R = dicVille["R"] #Revenu max depensable par l'ensemble des habitants   
    
    Qtm1 = dicVille["Qtm1"] #Quantite potentiellement consommee precedemment
    dM = S/(Nm+1) #distance hab-mcdo moyenne
    dK = S/(Nk+1)   

    Pk = Quick.pv + w*dK
    Pm = McDo.pv + w*dM
    travaux = False
    if Qtm1 == 0:
        travaux = True #Cas ou la ville n'a jamais eu de fast-food
        if Nm == 1: #Si mcdo s'est implante, alors:
            Qtm1 = R/McDo.pv
        if Nk == 1:
            Qtm1 = R/Quick.pv

    qM = Qtm1*(math.sqrt(Pk) + 1.5)/(Pm +1)*unouzero(Nm)
# ligne d'en dessous *0.98 (voir commentaire)
    qK = Qtm1*(math.sqrt(Pm) + 1.5)/(Pk +1)*unouzero(Nk)
    
    Qt = (qM + (R - Pm*qK)/Pk)*unouzero(Nm+Nk)

    return (qM,qK,Qt)
    
def profit(Qte,pv):
    """"Retourne le profit du restaurant ce mois-ci"""
    return Qte*(pv-coutMenu) - coutEntretien
    
def score(marque,ville):
    """Calcule la quantite de consommations si on implantait un restaurant ici"""
    newCarte = copy.deepcopy(carte)
    if int(carte[ville][marque]) != 0:
        newCarte[ville][marque] = int(carte[ville][marque]) + 1
    else:
        newCarte[ville][marque] = 1

    qM,qK,_ = fonctionDemande(newCarte,ville)

    if marque == "McDo":
        return profit(qM,McDo.pv) - McDo.dicProfit[ville]
    if marque == "Quick":
        return profit(qK,Quick.pv) - Quick.dicProfit[ville]
    
def MAJ():
    "Met a jour la quantite consommee et les profits"""
    QK,QM = 0,0
    dicProfitM = dict()
    dicProfitQ = dict()
    for ville in carte:
        qM,qK,carte[ville]["Qtm1"] = fonctionDemande(carte,ville) #MAJ des demandes
        QK += qK
        QM += qM
        dicProfitM[ville] = profit(qM,McDo.pv)*unouzero(carte[ville]["McDo"]) #Etude des profits
        dicProfitQ[ville] = profit(qK,Quick.pv)*unouzero(carte[ville]["Quick"])
    McDo.maj("Profits",dicProfitM)
    Quick.maj("Profits",dicProfitQ)
    print("nb Clients McDo:",QM,"  Nb Clients Quick:",QK)

def etude():
    dicScoreM = dict()
    dicScoreQ = dict()
    for ville in carte:
        dicScoreM[ville] = score("McDo",ville) #Etude des scores
        dicScoreQ[ville] = score("Quick",ville)
    Quick.maj("Scores",dicScoreQ)
    McDo.maj("Scores",dicScoreM)

def affichage():
    m = input("Partido:")
    if m == '':
        return ''
    if m == 'm':
        p = input("MacDonald's:")
        if p == 'nb':
            for i in carte:
                if carte[i]["McDo"] != 0:
                    print(i,":",carte[i]["McDo"])
        if p == 'nbp':
            for i in carte:
                if carte[i]["McDo"] == 0:
                    print(i,":",carte[i]["McDo"])
        if p == "sc":
            for i in McDo.dicScore:
                print(i,":",McDo.dicScore[i])
        if  p == 'b':
            print(McDo.epargne)
    if m == 'k':
        p = input("Quick:")
        if p == 'nb':
            for i in carte:
                if carte[i]["Quick"] != 0:
                    print(i,":",carte[i]["Quick"])
        if p == 'nbp':
            for i in carte:
                if carte[i]["Quick"] == 0:
                    print(i,":",carte[i]["Quick"])
        if p == "sc":
            for i in Quick.dicScore:
                print(i,":",Quick.dicScore[i])
        if p == 'b':
            print(Quick.epargne)
    if not(m == 'k' or m == 'm'):
        print("oh")
        return "FIN"
    return affichage()


#SUPERTEST
retMcDo = 0
retQuick = 1
modif = input("Modifier parametres, oui ou non?")
if modif == 'o' or modif == 'oui':
    retMcDo = int(input("Le retard du McDo sera de:"))
    retQuick = int(input("Le retard du Quick sera de:"))

k = False
m = False
num = 0

satsNbM = dict()
satsNbQ = dict()
satsEpargneM = dict()
satsEpargneQ = dict()
dicmap = dict()

caca = dict()
for i in carte:
    caca[i] = (0,0)
dicmap[0] = copy.deepcopy(caca)

M = ''
while M == '':
    print("Mois ",num,":")
    if num == retMcDo:
        m = True
    if num == retQuick:
        k = True

    etude()
    if m:
        McDo.choixNewResto()
        print("McDo a ",round(McDo.epargne),"€ et va implanter ici:",McDo.newResto)
    if k:
        Quick.choixNewResto()
        print("Quick a ",round(Quick.epargne),"€ et va implanter ici:",Quick.newResto)

    if m:
        McDo.imp()
        print("Implantation! McDo a paye",len(McDo.newResto)*coutImplantation,"€ et a maintenant",round(McDo.epargne),"€")
    if k:
        Quick.imp()
        print("Implantation! Quick a paye",len(Quick.newResto)*coutImplantation,"€ et a maintenant",round(Quick.epargne),"€")  
    satsNbM[num] = McDo.nbR
    satsNbQ[num] = Quick.nbR

    print("Mise jour des demandes")
    MAJ()
    if m:
        McDo.recolte()
        print("McDo a recolte ",round(McDo.profit),"€ et a maintenant " ,round(McDo.epargne),"€")
    if k:
        Quick.recolte()
        print("Quick a recolte ",round(Quick.profit),"€ et a maintenant " ,round(Quick.epargne),"€")

    avantM = McDo.epargne
    avantQ = Quick.epargne
    if  m:
        McDo.impots()
        print("McDo a paye ",round(-McDo.epargne + avantM),"€ aux impots et a maintenant ",round(McDo.epargne),"€")
    if k:
        Quick.impots()
        print("Quick a paye ",round(-Quick.epargne + avantQ),"€ aux impots et a maintenant ",round(Quick.epargne),"€")
    satsEpargneM[num] = McDo.epargne
    satsEpargneQ[num] = Quick.epargne

    print("\n","\n")
    M = affichage()
    num +=1
    for i in carte:
        caca[i] = (carte[i]["McDo"] ,carte[i]["Quick"])
    pipi =copy.deepcopy(caca)
    dicmap[num] = pipi
    
    
if input("Afficher courbes, oui ou non?") == "oui":
    plt.subplot(211)
    plt.plot([i for i in range(num)],[satsEpargneM[n] for n in range(num)],color="yellow", linewidth=2.5, linestyle="-", label="McDo")
    plt.plot([i for i in range(num)],[satsEpargneQ[n] for n in range(num)],color="red", linewidth=2.5, linestyle="-", label="Quick")
    plt.ylabel("Epargne (Euros)")
    plt.xlabel("Temps (mois)")
    plt.legend(loc='upper right', frameon=False)

    plt.subplot(212)
    plt.plot([i for i in range(num)],[satsNbM[n] for n in range(num)],color="yellow", linewidth=2.5, linestyle="-", label="McDo")
    plt.plot([i for i in range(num)],[satsNbQ[n] for n in range(num)],color="red", linewidth=2.5, linestyle="-", label="Quick")
    plt.ylabel("Nombre restaurants")
    plt.xlabel("Temps (mois)")
    plt.legend(loc='upper right', frameon=False)

    plt.show()

f = open("map.txt","w")
for i in dicmap:
    f.write("#" + str(i))
    f.write("\n")
    for j in dicmap[i]:
        a,b = dicmap[i][j]
        ligne =str(j)+","+str(a)+","+str(b)+"\n"
        f.write(ligne)
f.close()
#CONCLUSION
#C'est pas normal car mcdo a la meme evolution avec ou sans quick
#Il faut prendre en compte la preference et l'augmentation de R dans la consommation
#Il faut que mcdo et quick s'implantent plus, genre deux fois dans une meme ville
#changement de prix de vente reste a faire
#implantation trop rapide
#riche pauvres
#taille de la ville
#proximite avec autres villes
#tourisme
#publicite
#il faudrait rajouter le fait qu'ils doivent construire le mcdo et qu'ils ont un profit nul le premier mois
#voilaaaaa

#Commentaires des sistas
# en augmentant le taux d'imposition (de 0.20 à 0.80), même si le taux d'imposition est important, augmentation du nombre de Mac Do exponentielle
# Avec ou sans quick modification de 10000 $ seulement sur toute la France #caillouinutiledanslachaussure

# ON A REUSSI A COMPRENDRE TON PTN DE TEST !!!!!!!!!
# Quick evolue exactement comme Mc do (focntion demande craint?)
# si on met un coef de preference (type 0.98 de qK) on observe que Quick ouvre un resto avec un mois de retard dans une ville differente (#genial)
# la croissance est quand meme trop rapide (peut etre peut on imposer en fonction du revenu #paliers d'imposition sa mere)
#la prochaine fois met un putain de mode d'emploi 
