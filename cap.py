#Fabriquation du dictionnaire des villes
fichier = open("nomdufichier.txt")
liste_lignes = fichier.readlines()
carte = dict()
for ligne in liste_lignes:
	liste_de_mots = ligne.strip().split(",")
	a,b,c = liste_de_mots
	carte[a] = {"rev":b}
#a ville
#b revenu
#c nb hab
fichier.close()
for i in carte:
	carte[i]["rev"] = int(carte[i]["rev"])//12
#total c'est le ditctionnaire des villes

#FONCTIONS
def fonctionDemande(carte,ville,pref,pop,prix):
	"""Retourne le benefice en fonction des infos sur la ville"""
	nb = "jaa"
	return nb
    
def profit(nbConso, prix,coutMenu,coutEntretien):
  	""""Retourne le profit du restaurant ce moi-ci"""
	return nbConso*(prix-coutMenu) - coutEntretien
    
def score(carte,marque,ville,pref,pop,prix):
 	 """Calcule la quantité de consommations si on implantait un restaurant ici"""
	newVille = ville
	if ville[marque] == 0:
    	newVille = 1
	else:
    	newVille[marque] +=1
	return fonctionDemande(newVille,LERESTE!!!!!!!!!!!!!!!)


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
	


#CODE
def etude(carte, coutMenuM,coutMenuQ, coutEntretien, pop, pref, prixM,prixQ ):
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

