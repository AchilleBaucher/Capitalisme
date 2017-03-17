import math
import copy

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
tirelire = 0.8
moisAm = 12
moisnul = 10000
w = 0.1
coutMenu = 3
coutEntretien = 20000
coutImplantation = 800000
CompteM = 100000
CompteQ = 100000

#CLASSES

class Siege:
    def __init__(self,marque,pv,dicProfit,dicScore,epargne):
        self.marque = marque
        self.pv = pv
        self.dicProfit = dicProfit
        self.dicScore = dicScore
        self.epargne = epargne
        self.echec = "echec" + marque[0]

    def recolte(self):
        """Recolte les profits"""
        biff = 0
        for ville in self.dicProfit:
            biff += self.dicProfit[ville]
        self.epargne = (self.epargne+biff)*tirelire

    def desimp(self):
        """Desimplante et ajoute des malus si necesaire"""
        for ville in self.dicProfit:
            if carte[ville][self.marque] != 0 and dicProfit[ville]/carte[ville][self.marque]<moisnul :
                carte[ville][self.echec] += 1
            if carte[ville][self.echec] >= 12:
                carte[ville][self.marque] -= 1
                carte[ville][self.echec] = 0

    def imp(self):
        """Implante les nouveaux restaurants"""
        newResto = NewResto(self.epargne,EmplCool(self.dicScore))
        for ville in newResto:
            carte[ville][self.marque] += 1
        self.epargne -= len(newResto)*coutImplantation

    def maj(self,nomEl,newEl):
        if nomEl == "Profits":
            self.dicProfit = newEl
        elif nomEl == "Scores":
            self.dicScore = newEl

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

def NewResto(biff,dicEmplCool):
    """Renvoie la liste des emplacements qui recevront un restaurant"""
    NewResto = set()
    nbMax = biff // coutImplantation
    e = 0
    fort = 0
    best = ""
    while e<=nbMax:
        for ville in dicEmplCool:
            print
            if not(ville in NewResto):
                if dicEmplCool[ville]>fort:
                        fort=dicEmplCool[ville]
                        best=ville
        NewResto.add(best)
        e+=1
        fort = 0
        best = ""

    return NewResto

def unouzero(n):
    if n == 0:
        return 0
    return 1

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

    Pk = pVK + w*dK
    Pm = pVM + w*dM

    if Qtm1 == 0: #Cas ou la ville n'a jamais eu de fast-food
        if Nm == 1: #Si mcdo s'est implante, alors:
            Qtm1 = R/pVM
        if Nk == 1:
            Qtm1 = R/pVK

    qM = Qtm1*(math.sqrt(Pk) + 1.5)/(Pm +1)*unouzero(Nm) 

    qK = Qtm1*(math.sqrt(Pm) + 1.5)/(Pk +1)*unouzero(Nk)
    
    Qt = (qM + (R - Pm*qM)/Pk)*unouzero(Nm+Nk)

    return (qM,qK,Qt)

#Prendre en compte la preference et l'augmentation de R dans la consommation
    
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
        return profit(qM,pVM)
    if marque == "Quick":
        return profit(qK,pVK)
    
def MAJ():
    "Met a jour la quantite consommee et les profits"""
    dicProfitM = dict()
    dicProfitQ = dict()
    for ville in carte:
        qM,qK,carte[ville]["Qtm1"] = fonctionDemande(carte,ville) #MAJ des demandes
        dicProfitM[ville] = profit(qM,pVM)*unouzero(carte[ville]["McDo"]) #Etude des profits
        dicProfitQ[ville] = profit(qK,pVK)*unouzero(carte[ville]["Quick"])
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

#TEST
m = ''
while m == '':
    etude()
    McDo.imp()
    print(carte["Paris1"]["McDo"],carte["Paris1"]["Qtm1"])
    MAJ()
    McDo.recolte()
    print(McDo.epargne)
    m = input("UN MOIS DEJA:")