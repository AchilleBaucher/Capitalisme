#C'est pour modifier les villes.

#POUR AJOUTER DES VIRGULES:
"""
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
new_liste = []
for i in liste_lignes:
	a = i[:-2] + ","
	new_liste.append(a)
fichier.close()
print(new_liste[0])

fichier = open("villes.txt","wcd")
for i in new_liste:
	fichier.write(i)
	fichier.write("\n")
fichier.close"""

#POUR RETIRER DES VIRGULES
"""
fichier = open("villes.txt")
liste_lignes = fichier.readlines()
new_liste = []
for i in liste_lignes:
	a = i[:-3]
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
