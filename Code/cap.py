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
    carte[Nom] = {"rev":int(Rev),"nbHab":int(nbHab),"Rsurface":float(Rsurface),"McDo":int(McDo),"Quick":int(Quick),"echecM":int(echecM),"echecQ":int(echecQ),"R":float(R),"Qtm1":int(Qtm1)}

fichier.close()

#Donnees
pVK = 8
pVM = 8
tirelire = 0.5
moisAm = 12
moisnul = 10000
w = 0.3
coutMenu = 5
coutEntretien = 30000
coutImplantation = 800000
CompteM = 800000
CompteQ = 800000

#CLASSES

class Siege:
    def __init__(self,marque,pv,dicProfit,dicScore,epargne):
        self.marque = marque
        self.pv = pv
        self.dicProfit = dicProfit
        self.dicScore = dicScore
        self.epargne = epargne
        self.echec = "echec" + marque[0]
        self.newResto = set()
        self.mois = 0
        self.profit = 0

    def recolte(self):
        """Recolte les profits"""
        biff = 0
        for ville in self.dicProfit:
            biff += self.dicProfit[ville]
        self.profit = biff
        self.epargne = self.epargne+biff

    def desimp(self):
        """Desimplante et ajoute des malus si necesaire"""
        for ville in self.dicProfit:
            if carte[ville][self.marque] != 0 and dicProfit[ville]/carte[ville][self.marque]<moisnul :
                carte[ville][self.echec] += 1
            if carte[ville][self.echec] >= 12:
                carte[ville][self.marque] -= 1
                carte[ville][self.echec] = 0

    def choixNewResto(self):
        """Renvoie la liste des emplacements qui recevront un restaurant"""
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
        self.epargne -= len(self.newResto)*coutImplantation

    def maj(self,nomEl,newEl):
        if nomEl == "Profits":
            self.dicProfit = newEl
        elif nomEl == "Scores":
            self.dicScore = newEl
    def impots(self):
        self.epargne = self.epargne*0.8

#Creation des Sieges
dic = dict()
for ville in carte:
    dic[ville] = 0

McDo = Siege("McDo",pVM,dic,dic,CompteM)
Quick = Siege("Quick",pVK,dic,dic,CompteQ)

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

    if Qtm1 == 0: #Cas ou la ville n'a jamais eu de fast-food
        if Nm == 1: #Si mcdo s'est implante, alors:
            Qtm1 = R/McDo.pv
        if Nk == 1:
            Qtm1 = R/Quick.pv

    qM = Qtm1*(math.sqrt(Pk) + 1.5)/(Pm +1)*unouzero(Nm) 

    qK = Qtm1*(math.sqrt(Pm) + 1.5)/(Pk +1)*unouzero(Nk)
    
    Qt = (qM + (R - Pm*qM)/Pk)*unouzero(Nm+Nk)

    return (qM,qK,Qt)
    
def profit(Qte,pv):
    """"Retourne le profit du restaurant ce moi-ci"""
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
    dicProfitM = dict()
    dicProfitQ = dict()
    for ville in carte:
        qM,qK,carte[ville]["Qtm1"] = fonctionDemande(carte,ville) #MAJ des demandes
        dicProfitM[ville] = profit(qM,McDo.pv)*unouzero(carte[ville]["McDo"]) #Etude des profits
        dicProfitQ[ville] = profit(qK,Quick.pv)*unouzero(carte[ville]["Quick"])
    McDo.maj("Profits",dicProfitM)
    Quick.maj("Profits",dicProfitQ)

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


#TEST
kik = input("Quick est'il de la partie?")
if kik == "O" or kik == "oui" or kik == "o" or kik == "Oui" or kik == "y" or kik == "yes":
    k = True
else:
    k = False
num = 0
m = ''
while m == '':
    print("Mois ",num,":")
    etude()
    McDo.choixNewResto()
    if k:
        Quick.choixNewResto()
    print("McDo a ",round(McDo.epargne),"€ et va implanter ici:",McDo.newResto)
    McDo.imp()
    if k:
        Quick.imp()
    print("Implantation! McDo a paye",len(McDo.newResto)*coutImplantation,"€ et a maintenant",round(McDo.epargne),"€")
    MAJ()
    print("Mise jour des demandes")
    McDo.recolte()
    if k:
        Quick.recolte()
    avant = McDo.epargne
    print("McDo a recolte ",round(McDo.profit),"€ et a maintenant " ,round(McDo.epargne),"€")
    McDo.impots()
    if k:
        Quick.impots()
    print("McDo a paye ",round(-McDo.epargne + avant),"€ aux impots et a maintenant ",round(McDo.epargne),"€","\n","\n")
    m = affichage()
    num +=1








#satsProfitM = dict()
#satsProfitM[0] = McDo.dicProfit
#satsProfitM[0]["Profit total"] = McDo.epargne
#satsProfitQ = dict()
#satsProfitQ[0] = Quick.dicProfit
#satsProfitQ[0]["Profit total"] = Quick.epargne

#statsNb = dict()

#Quick.recolte()
#satsProfitM[num] = McDo.dicProfit
#satsProfitM[num]["Epargne"] = McDo.epargne
#satsProfitQ[num] = Quick.dicProfit
#satsProfitQ[num]["Epargne"] = Quick.epargne
#num+=1
#m = affichage()

#plt.plot([i for i in range(num)],[satsProfitM[n]["Epargne"] for n in range(num)],color="yellow", linewidth=2.5, linestyle="-", label="McDo") #bleu
#plt.plot([i for i in range(num)],[satsProfitQ[n]["Epargne"] for n in range(num)],color="red", linewidth=2.5, linestyle="-", label="Quick") #bleu
#plt.xlabel("Epargne")
#plt.legend(loc='upper right', frameon=False)
#plt.xlabel("Temps (mois)")
#plt.ylabel("Epargne (Euros)")
#plt.show()

#CONCLUSION
#C'est pas normal car mcdo a la meme evolution avec ou sans quick
#Il faut prendre en compte la preference et l'augmentation de R dans la consommation
#Il faut que mcdo et quick s'implantent plus, genre deux fois dans une meme ville
#changement de prix de vente reste a faire
#implantation trop rapide
#riche pauvres
#taile de la ville
#proximite avec autres villes
#tourisme
#publiite
#il faudrait rajouter le fait qu'ils doivent construire le mcdo et qu'ils ont un profit nul le premier mois
#voilaaaaa
