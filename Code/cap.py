import math
import copy
#Fabriquation du dictionnaire des villes
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
carte = dict()
for ligne in liste_lignes:
    liste_de_mots = ligne.strip().split(",")
    Nom,Rev,nbHab,Rsurface,McDo,Quick,echecM,echecQ,Qtm1,R = liste_de_mots
    carte[Nom] = {"rev":Rev,"nbHab":nbHab,"Rsurface":Rsurface,"McDo":McDo,"Quick":Quick,"echecM":echecM,"echecQ":echecQ,"R":R,"Qtm1":Qtm1}

fichier.close()

#CLASSES

class Restaurant:
    def __init__(self,marque,ville):
        self.marque = marque
        self.ville = ville
        self.conso = conso
        
class Siege:
    def __init__(self,coutEntretien,marque,popularite,prixMenu,prixOuverture):
        self.marque = marque
        self.pop = popularite
        self.prixOuv = prixOuverture
        self.prixMen = prixMenu
        self.coutEnt = coutEntretien

#FONCTIONS
def fonctionDemande(carte,ville,pref,pVm,pVK,w):
    """Retourne la Qte de consommations de menus Quick et McDo en fonction des infos sur la ville"""
    dicVille = carte[ville]
    Nm = int(dicVille["McDo"]) #Nombre de McDo dans la ville
    Nk = int(dicVille["Quick"]) # ref Quick

    S = float(dicVille["Rsurface"]) #Qui est la racine carree de la surface
    R = float(dicVille["R"]) #Revenu max depensable par l'ensemble des habitants
    
    
    Qtm1 = float(dicVille["Qtm1"]) #Quantite consommee precedent
    dM = S/(Nm+1) #distance hab-mcdo moyenne
    dK = S/(Nk+1)   

    Pk = pVK + w*dK
    Pm = pVm + w*dM
    if Nm == 0:
        qM = 0
    else:
        qM = Qtm1*(math.sqrt(Pk) + 1.5)/(Pm +1)
    if Nk == 0:
        qK = 0
    else:
        qK = Qtm1*(math.sqrt(Pm) + 1.5)/(Pk +1) 
    
    Qt = qM + (R - Pm*qM)/Pk
    
    dicVille["Qtm1"] = Qt
    
    return (qM,qK)

#Prendre en compte la preference et l'ugmentation de R dans la consommation
    
def profit(nbConso,pv,coutMenu,coutEntretien):
    """"Retourne le profit du restaurant ce moi-ci"""
    return nbConso*(pv-coutMenu) - coutEntretien
    
def score(carte,marque,ville,pVM,pVK,w):
    """Calcule la quantite de consommations si on implantait un restaurant ici"""
    newCarte = copy.deepcopy(carte)
    if int(carte[ville][marque]) != 0:
        newCarte[ville][marque] = int(carte[ville][marque]) + 1
    else:
        newCarte[ville][marque] = 1

    qM,qK = fonctionDemande(newCarte,ville,pVM,pVK,w)
    if marque == "McDo":
        return qM
    if marque == "Quick":
        return qK
    
def etude(carte, coutMenuM,coutMenuQ, coutEntretien, pVM,pVK,w ):
    "Renvoie pour chaque ville son profit et son score"""
    dicProfit = dict()
    dicScoreM = dict()
    dicScoreQ = dict()
    for ville in carte:
        dicScoreM[ville] = score(carte,"Mcdo",ville, pVM,pVK,w)
        dicScoreQ[ville] = score(carte,"Quick",ville,  pVM,pVK,w)
        dicProfitM[ville] = profit(ville["nbConso"], pvM,coutMenuM,coutEntretien)*(ville["Mcdo"])
        dicProfitQ[ville] = profit(ville["nbConso"], pvQ,coutMenuQ,coutEntretien)*(ville["Quick"])
    return (dicScoreM, dicScoreQ, dicProfitM, dicProfitQ)

def decisionM(tirelire,carte, pop, pref, dicScoreM, dicProfitM, coutImplantation,Compte_epargne):
    """Renvoie la decicsion mensuelle des sieges"""
    a=0
    b=0
    c=0
    d=0
    NewRestoM=dict()
    dicEmplCoolM=dict()
    cartebis=copy.deepcopy(carte)
    for i in dicProfitM:
        a+=i
    biff=a*tirelire
    #desimplantation
    for i in dicProfitM:
        if i<moisnul:
                echecM+=1
        if echecM==12:
                cartebis[i]["McDo"]=cartebis[i]["McDo"]-1
    #implantation
    if biff>=coutImplantation:
        for i in dicScoreM:
            if i*12>=coutImplantation:
                dicEmplCoolM[ville]=i
            b=biff//coupImplantation
    e = 0
    while e<=b:
        for i in dicEmplCoolM:
            if not( i in NewRestoM):
                if dicEmplCoolM[i]>c:
                        c=dicEmplCoolM[i]
                        d=i
            NewRestoM[d]=c
        e+=1
        c=0
        d=0
    Compte_epargne+=(a-biff)+(biff-b*coutImplantation)
    return(cartebis,NewRestoM)

def decisionQ(tirelire,carte, dicScoreQ, dicProfitQ,coutImplantation,Compte_epargne):
    """Renvoie la decicsion mensuelle des sieges"""
    a=0
    b=0
    c=0
    d=0
    NewRestoQ=dict()
    dicEmplCoolQ=dict()
    cartebis2=copy.deepcopy(carte)
    for i in dicProfitQ:
        a+=i
    biff=a*tirelire
    #desimplantation
    for i in dicProfitQ:
        if i<moisnul:
                echecQ+=1
        if echecM==12:
                cartebis2[i]["Quick"]=cartebis2[i]["Quick"]-1
    #implantation
    if biff>=coutImplantation:
        for i in dicScoreQ:
            if i*12>=coutImplantation:
                dicEmplCoolQ[ville]=i
            b=biff//coupImplantation
    e = 0
    while e<=b:
        for i in dicEmplCoolQ:
            if not( i in NewRestoQ):
                if dicEmplCoolQ[i]>c:
                        c=dicEmplCoolQ[i]
                        d=i
            NewRestoQ[d]=c
        e+=1
        c=0
        d=0
    Compte_epargne+=(a-biff)+(biff-b*coutImplantation)
    return(cartebis2,NewRestoQ)
    
def action (cartebis,cartebis2,carte):
    #desimplantation
    for ville in carte:
        carte[ville]['Mcdo']=cartebis[ville]['Mcdo']
        carte[ville]['Quick']=cartebis2[ville]['Quick']
    #implantation
    for i in NewRestoM:
        carte[i]['Mcdo']+=1
    for i in NewRestoQ:
        carte[i]['Quick']+=1
    return carte
dicScoreM, dicScoreQ, dicProfitM, dicProfitQ = etude(carte,3,3,20000,8,8,0.1)
print(decisionQ(0.8,carte,dicScoreQ,dicProfitQ,800000,6))
