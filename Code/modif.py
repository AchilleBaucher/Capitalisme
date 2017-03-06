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
