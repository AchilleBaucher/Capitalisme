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
def fonctionDemande(carte,ville,pref,pop,prix):
	"""Retourne le benefice en fonction des infos sur la ville"""
	dicVille = carte[ville]
	Nm = dicVille["McDo"]
	Nk = dicVille["Quick"]
	Pm = dicVille["PrixM"]
	Pk = dicVille["PrixQ"]
	S = dicVille["Surface"]
	dM = S/Nm
	dK = S/Nk

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

	return nb
    
def profit(nbConso, prix,coutMenu,coutEntretien):
  	""""Retourne le profit du restaurant ce moi-ci"""
	return nbConso*(prix-coutMenu) - coutEntretien
    
def score(carte,marque,ville,pref,pop,prix):
 	"""Calcule la quantite de consommations si on implantait un restaurant ici"""
	newVille = ville
	if ville[marque] == 0:
		newVille[mrque] =1
	else:
		newVille[marque] +=1
	return fonctionDemande(carte,newVille,pref,pop,prix)

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
