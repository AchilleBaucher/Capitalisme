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
#modification 
for i in carte:
    carte[i]["Qtm1"] = carte[i]["R"]/pVK
#Donnees
pVK = 8
pVM = 8
tirelire = 0.8
moisAm = 12
moisnul = 10000
w = 0.1
coutMenu = 3
coutEntretien = 20000
coutImplantation = 800000000000
CompteM = 10000000000000000
CompteQ = 1000000000000000
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
def fonctionDemande(carte,ville,pVM,pVK,w):
    """Retourne la Qte de consommations de menus Quick et McDo en fonction des infos sur la ville"""
    dicVille = copy.deepcopy(carte[ville])
    Nm = int(dicVille["McDo"]) #Nombre de McDo dans la ville
    Nk = int(dicVille["Quick"]) # ref Quick

    S = float(dicVille["Rsurface"]) #Qui est la racine carree de la surface
    R = float(dicVille["R"]) #Revenu max depensable par l'ensemble des habitants
    
    
    Qtm1 = float(dicVille["Qtm1"]) #Quantite consommee precedent
    dM = S/(Nm+1) #distance hab-mcdo moyenne
    dK = S/(Nk+1)   

    Pk = pVK + w*dK
    Pm = pVM + w*dM
    if Nm == 0:
        qM = R / pVM
    else:
        qM = Qtm1*(math.sqrt(Pk) + 1.5)/(Pm +1)

    if Nk == 0:
        qK = R / pVK
    else:
        qK = Qtm1*(math.sqrt(Pm) + 1.5)/(Pk +1) 
    
    Qt = qM + (R - Pm*qM)/Pk
    
    dicVille["Qtm1"] = Qt
    
    return (qM,qK)

#Prendre en compte la preference et l'ugmentation de R dans la consommation
    
def profit(nbConso,pv,coutMenu,coutEntretien):
    """"Retourne le profit du restaurant ce moi-ci"""
    return nbConso*(pv-coutMenu) - coutEntretien
    
def score(carte,marque,ville,pVM,pVK,w,coutMenu,coutEntretien):
    """Calcule la quantite de consommations si on implantait un restaurant ici"""
    newCarte = copy.deepcopy(carte)
    if int(carte[ville][marque]) != 0:
        newCarte[ville][marque] = int(carte[ville][marque]) + 1
    else:
        newCarte[ville][marque] = 1

    qM,qK = fonctionDemande(newCarte,ville,pVM,pVK,w)
    if marque == "McDo":
        return profit(qM,pVM,coutMenu,coutEntretien)
    if marque == "Quick":
        return profit(qK,pVK,coutMenu,coutEntretien)
    
def etude(carte, coutMenuM,coutMenuQ, coutEntretien, pVM,pVK,w):
    "Renvoie pour chaque ville son profit et son score"""
    dicProfitM = dict()
    dicProfitQ = dict()
    dicScoreM = dict()
    dicScoreQ = dict()
    for ville in carte:
        dicScoreM[ville] = score(carte,"McDo",ville, pVM,pVK,w,coutMenu,coutEntretien)
        dicScoreQ[ville] = score(carte,"Quick",ville, pVM,pVK,w,coutMenu,coutEntretien)
        dicProfitM[ville] = profit(carte[ville]["Qtm1"], pVM,coutMenu,coutEntretien)*(carte[ville]["McDo"])
        dicProfitQ[ville] = profit(carte[ville]["Qtm1"], pVK,coutMenu,coutEntretien)*(carte[ville]["Quick"])
    return (dicScoreM, dicScoreQ, dicProfitM, dicProfitQ)

def decisionM(tirelire,moisAm,moisnul,carte, dicScoreM, dicProfitM, coutImplantation,Compte_epargne):
    """Renvoie la decicsion mensuelle des sieges"""
    a=0#profit total
    b=0
    c=0
    d=0
    NewRestoM=dict()
    dicEmplCoolM=dict()
    cartebis=copy.deepcopy(carte)
    for i in dicProfitM:
        a+=dicProfitM[i]
    biff=a*tirelire
    #desimplantation
    for i in dicProfitM:
        if carte[i]["McDo"] != 0 and dicProfitM[i]/carte[i]["McDo"]<moisnul :
                cartebis[i]["echecM"]+=1
        if echecM == moisAm:
                cartebis[i]["McDo"]=cartebis[i]["McDo"]-1
    #implantation
    if biff>=coutImplantation:
        for i in dicScoreM:
            if dicscoreM[i]*moisAm>=coutImplantation:
                dicEmplCoolM[ville]=i
    b=biff//coutImplantation
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

def decisionQ(tirelire,moisAm,moisnul,carte, dicScoreQ, dicProfitQ,coutImplantation,Compte_epargne):
    """Renvoie la decicsion mensuelle des sieges"""
    a=0
    b=0
    c=0
    d=0
    NewRestoQ=dict()
    dicEmplCoolQ=dict()
    cartebis2=copy.deepcopy(carte)
    for i in dicProfitQ:
        a+=dicProfitQ[i]
    biff=a*tirelire + Compte_epargne
    #desimplantation
    for i in dicProfitQ:
        if carte[i]["Quick"] != 0 and dicProfitQ[i]/carte[i]["Quick"]<moisnul :
                cartebis2[i]["echecQ"]+=1
        if echecM==moisAm:
                cartebis2[i]["Quick"]=cartebis2[i]["Quick"]-1
    #implantation
    print(biff,coutImplantation)
    if biff>=coutImplantation:
        for i in dicScoreQ:
            if i == "Paris1":
                print("JFGC3",dicScoreQ[i],moisAm,coutImplantation)
            if dicScoreQ[i]*moisAm>=coutImplantation:
                dicEmplCoolQ[i]=dicScoreQ[i]
    print(dicEmplCoolQ)
    b=biff//coutImplantation
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
    
def action (cartebis,NewRestoM,NewRestoQ,cartebis2,carte):
    #desimplantation
    for ville in carte:
        carte[ville]['McDo']=cartebis[ville]['McDo']
        carte[ville]['Quick']=cartebis2[ville]['Quick']
    return carte

def main(carte, pVK,pVM,tirelire,moisAm,moisnul,w, coutMenuM, coutMenuQ,coutEntretien, coutImplantation,CompteM,CompteQ,maxit):
    """Fait toute la simulation"""
    for i in range(maxit):
        dicScoreM, dicScoreQ, dicProfitM, dicProfitQ = etude(carte, coutMenuM,coutMenuQ, coutEntretien, pVM,pVK,w)
        cartebisM, NewRestoM = decisionM(tirelire,moisAm,moisnul,carte, dicScoreM, dicProfitM, coutImplantation,CompteM) #RAJOUTER PRIX DE VENTE
        print(NewRestoM)
        cartebisQ , NewRestoQ = decisionQ(tirelire,moisAm,moisnul,carte, dicScoreQ, dicProfitQ,coutImplantation,CompteQ) 
        print(NewRestoQ)
        carte = copy.deepcopy(action(cartebisM,NewRestoM,NewRestoQ,cartebisQ,copy.deepcopy(carte)))

carr  = copy.deepcopy(carte)
carr["Paris1"]["Quick"] = 1
tQM,tQK = fonctionDemande(carr,"Paris1",pVM,pVK,w)
#print("Qte: ",profit(tQM,pVM,coutMenu,coutEntretien))
#print(score(carte,"Quick","Paris1",pVM,pVK,w,coutMenu,coutEntretien))
_,caca,_,jh = etude(carte,3,3, coutEntretien, pVM,pVK,w)
#print(caca["Paris1"])
a,b=decisionQ(tirelire,moisAm,moisnul,carte, caca, jh,coutImplantation,CompteQ)

#print(a['Paris1'],b)
#main(carte, pVK,pVM,tirelire,moisAm,moisnul,w, coutMenuM, coutMenuQ,coutEntretien, coutImplantation,CompteM,CompteQ,12)
#mmh = open("testVi.txt","w")
#main(carte, pVK,pVM,tirelire,moisAm,moisnul,w, coutMenuM, coutMenuQ,coutEntretien, coutImplantation,CompteM,CompteQ,24)
