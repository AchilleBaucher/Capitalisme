import math
#Fabriquation du dictionnaire des villes
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
carte = dict()
for ligne in liste_lignes:
	liste_de_mots = ligne.strip().split(",")
	a,b,c = liste_de_mots
	carte[a] = {"rev":b}
#a ville
#b revenu
#c nombre d'habitants
fichier.close()
for i in carte:
	carte[i]["rev"] = int(carte[i]["rev"])//12
#carte c'est le ditctionnaire des villes


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
def fonctionDemande(carte,ville,pref,pop,w):
	"""Retourne le benefice en fonction des infos sur la ville"""
	dicVille = carte[ville]
	Nm = dicVille["McDo"]
	Nk = dicVille["Quick"]

	S = dicVille["Surface"] #Qui est en fait sqrt(suface)
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
"""    Pour la fonction demande:
qm(t)=Q(t-1)*(sqrt(Pk)+1.5)/(pm+1)           
qk(t)=Q(t-1)*(sqrt(Pm)+1.5)/(pk+1)
pk=pvk+w*(sqrt(S)/nk)
pm=pvm+w*(sqrt(S)/nm)
w poids du transport dans le cout total
pvk=pvm prix de vente 
Contrainte de revenu
pk*qk+pm*qm=R
R part de revenu par fast food=3 pourcents du revenu total
Q=qk+qm (demande totale)
donc Q(t)=qm(t)+((R-pm*qm(t))/pk)"""
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
	
def etude(carte, coutMenuM,coutMenuQ, coutEntretien, pop, pref, prixM,prixQ ):
	"Renvoie pour chaque ville son profit et son score"""
	dicProfit = dict()
	dicScoreM = dict()
	dicScoreQ = dict()
	for ville in carte:
		dicScoreM[ville] = score(carte,"Mcdo",ville,pref, pop, prix)
		dicScoreQ[ville] = score(carte,"Quick",ville,pref, pop, prix)
		dicProfitM[ville] = profit(ville["nbConso"], prixM,coutMenuM,coutEntretien)*(ville["Mcdo"])
		dicProfitQ[ville] = profit(ville["nbConso"], prixQ,coutMenuQ,coutEntretien)*(ville["Quick"])
	return (dicScoreM, dicScoreQ, dicProfitM, dicProfitQ)

def decision(carte, pop, pref, dicScoreM, dicScoreQ, dicProfitM, dicProfitQ):
	"""Renvoie la decicsion mensuelle des sieges"""
