#C'est pour modifier les villes.
import math

#POUR AJOUTER DES DONNEES:
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
new_liste = []
b = 0
for i in liste_lignes:
	liste_de_mots = i.strip().split(",")
	new_liste.append(int(liste_de_mots[2])/float(liste_de_mots[3])/1000)
for i in new_liste:
	b += i
print(new_liste)
print(b/len(new_liste))


#POUR MODIFIER DES ATTRIBUTS
"""
numeroAttribut = 3
def operation(attribut):
	return math.sqrt(attribut)
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
new_liste = []
for i in liste_lignes:
	liste_de_mots = i.strip().split(",")
	attribut = liste_de_mots[numeroAttribut]
	a = ''
	el = operation(float(attribut))
	for at in liste_de_mots[:numeroAttribut] :
		a = a + at +','
	a = a + str(el)
	for at in liste_de_mots[numeroAttribut+1:] :
		a = a +',' + at
	new_liste.append(a)
fichier.close()

fichier = open("villes.txt","wcd")
for i in new_liste:
	fichier.write(i)
	fichier.write("\n")
fichier.close
"""

#POUR RETIRER DES VIRGULES
"""
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
new_liste = []
for i in liste_lignes:
	a = i[:-2]
	new_liste.append(a)
fichier.close()
print(new_liste[0])

fichier = open("villes.txt","wcd")
for i in new_liste:
	fichier.write(i)
	fichier.write("\n")
fichier.close
"""
#Pour taper les attributs:
"""
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
new_liste = []
for i in liste_lignes:
	liste_de_mots = i.strip().split(",")
	ville = liste_de_mots[0]
	b = raw_input((ville+":"))
	a = i[:-2] + ',' + b
	new_liste.append(a)
fichier.close()
print(new_liste[0])

fichier = open("villes.txt","wcd")
for i in new_liste:
	fichier.write(i)
	fichier.write("\n")
fichier.close"""
