import math
#Fabriquation du dictionnaire des villes
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
carte = dict()
for ligne in liste_lignes:
	liste_de_mots = ligne.strip().split(",")
	Nom,Rev,nbHab,Rsurface,McDo,Quick,Qtm1,acc,R = liste_de_mots
	carte[Nom] = {"rev":Rev,"nbHab":nbHab,"Rsurface":Rsurface,"McDo":McDo,"Quick",:Quick,"Qtm1":Qtm1,"acc":acc,"R":R}

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
def fonctionDemande(carte,ville,pref,w):
	"""Retourne la Qte de consommations de menus Quick et McDo en fonction des infos sur la ville"""
	dicVille = carte[ville]
	Nm = dicVille["McDo"] #Nombre de McDo dans la ville
	Nk = dicVille["Quick"] # ref Quick

	S = dicVille["Rsurface"] #Qui est la racine carree de la surface
	R = dicVille["R"] #Revenu max depensable par l'ensemble des habitants
	
	Qtm1 = dicville["Qtm1"] #Quantite consommee precedent
	dM = S/Nm #distance hab-mcdo moyenne
	dK = S/Nk   

	Pk = pVK + w*dK
	Pm = pVm + w*dM
	
	qM = Qtm1*(math.sqrt(Pk) + 1.5)/(Pm +1) 
	qK = Qtm1*(math.sqrt(Pm) + 1.5)/(Pk +1) 
	
	Qt = qM + (R - Pm*qM)/Pk
	
	dicVille["Qtm1"] = Qt
	
	return (qM,qK)

#Modification dans le cas ou il n'y a ni McDo ni Quick
#Prendre en compte la préférence et l'ugmentation de R dans la consommation
    
def profit(nbConso,pv,coutMenu,coutEntretien):
  	""""Retourne le profit du restaurant ce moi-ci"""
	return nbConso*(pv-coutMenu) - coutEntretien
    
def score(carte,marque,ville,pref,pop,pv):
 	"""Calcule la quantite de consommations si on implantait un restaurant ici"""
	newVille = ville
	if ville[marque] == 0:
		newVille[marque] =1
	else:
		newVille[marque] +=1
	
	qM,qK = fonctionDemande(carte,newVille,pref,pop,prix)
	if marque == "McDo":
		return qM
	if marque == "Quick":
		return qK
	
def etude(carte, coutMenuM,coutMenuQ, coutEntretien, pop, pref, pvM,pvQ ):
	"Renvoie pour chaque ville son profit et son score"""
	dicProfit = dict()
	dicScoreM = dict()
	dicScoreQ = dict()
	for ville in carte:
		dicScoreM[ville] = score(carte,"Mcdo",ville,pref, pop, pvM)
		dicScoreQ[ville] = score(carte,"Quick",ville,pref, pop, pvQ)
		dicProfitM[ville] = profit(ville["nbConso"], pvM,coutMenuM,coutEntretien)*(ville["Mcdo"])
		dicProfitQ[ville] = profit(ville["nbConso"], pvQ,coutMenuQ,coutEntretien)*(ville["Quick"])
	return (dicScoreM, dicScoreQ, dicProfitM, dicProfitQ)

def decision(carte, pop, pref, dicScoreM, dicScoreQ, dicProfitM, dicProfitQ):
	"""Renvoie la decicsion mensuelle des sieges"""
