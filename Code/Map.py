from tkinter import*

#Page
Pageprincipale = Tk()
Pageprincipale.geometry ("1200x900+65+50")
Pageprincipale.title('Carte McDo/Quick')
Pageprincipale.maxsize (width=728,height=589)
Pageprincipale.minsize (width=728,height=589)
Pageprincipale['bg']='Black'

#photo
PhotoIDF = PhotoImage(file="Carte Île de france.png")

#Fond
canvas = Canvas(Pageprincipale,width=728, height=589)


#Création des villes:

Paris1 = canvas.create_rectangle(309,206,310,207)
Paris2 = canvas.create_rectangle(309,204,310,205)
Paris3 = canvas.create_rectangle(311,204,312,205)
Paris4 = canvas.create_rectangle(311,206,312,210)
Paris5 = canvas.create_rectangle(310,211,312,213)
Paris6 = canvas.create_rectangle(309,209,310,213)
Paris7 = canvas.create_rectangle(290,203,302,208)
Paris8 = canvas.create_rectangle(290,198,298,202)
Paris9 = canvas.create_rectangle(299,198,309,201)
Paris10 = canvas.create_rectangle(309,198,315,201)
Paris11 = canvas.create_rectangle(313,200,322,208)
Paris12 = canvas.create_rectangle(317,215,345,220)
Paris13 = canvas.create_rectangle(311,215,318,225)
Paris14 = canvas.create_rectangle(305,215,311,225)
Paris15 = canvas.create_rectangle(282,213,295,223)
Paris16 = canvas.create_rectangle(275,200,282,223)
Paris17 = canvas.create_rectangle(290,185,303,193)
Paris18 = canvas.create_rectangle(303,185,312,193)
Paris19 = canvas.create_rectangle(313,185,322,195)
Paris20 = canvas.create_rectangle(325,200,330,208)

StDenis = canvas.create_rectangle(308,162,311,183)
BoulogneBilancourt = canvas.create_rectangle(268,211,275,220)
Versailles = canvas.create_rectangle(235,230,250,240)
Creteil = canvas.create_rectangle(335,230,345,240)
NeuillySurSeine = canvas.create_rectangle(280,185,290,190)
Cergy = canvas.create_rectangle(202,115,220,125)
Rambouillet = canvas.create_rectangle(
Meaux= canvas.create_rectangle(
Evry= canvas.create_rectangle(
Orsay= canvas.create_rectangle(
Melun= canvas.create_rectangle(
Etampes= canvas.create_rectangle(
Goussainville= canvas.create_rectangle(
Poissy= canvas.create_rectangle(
Villepinte= canvas.create_rectangle(
Coulommiers= canvas.create_rectangle(
Claye-Souilly= canvas.create_rectangle(
Brie-Comte-Robert= canvas.create_rectangle(
Dourdan= canvas.create_rectangle(
Gretz-Armainvilliers= canvas.create_rectangle(
Thoiry= canvas.create_rectangle(
L’Isle-Adam= canvas.create_rectangle(
Magny-en-Vexin= canvas.create_rectangle(
Les Mureaux= canvas.create_rectangle(
Limay= canvas.create_rectangle(
Montereau-Fault-Yonne= canvas.create_rectangle(
Provins= canvas.create_rectangle(
Nemours= canvas.create_rectangle(
Guyancourt= canvas.create_rectangle(
Elancourt= canvas.create_rectangle(
Chessy= canvas.create_rectangle(
Nangis= canvas.create_rectangle(
Issy-les-Moulineux= canvas.create_rectangle(
La Ferté-sous-Jouarre= canvas.create_rectangle(
Noisy-le-grand= canvas.create_rectangle(
Saint-Germain-en-Laye= canvas.create_rectangle(
La Celle-saint-Cloud= canvas.create_rectangle(
Rosny-sous-Bois= canvas.create_rectangle(
Franconville= canvas.create_rectangle(
Gonesse= canvas.create_rectangle(
Villiers-sur-Marne= canvas.create_rectangle(
Torcy= canvas.create_rectangle(
Plaisir= canvas.create_rectangle(
Palaiseau= canvas.create_rectangle(
Mantes-la-Jolie= canvas.create_rectangle(
Sarcelles= canvas.create_rectangle(
Le Perray-en-Yvelines= canvas.create_rectangle(
Dammartin-en-Goele= canvas.create_rectangle(
Serris= canvas.create_rectangle(
Bombon= canvas.create_rectangle(
Bretigny-sur-orge= canvas.create_rectangle(
Avon= canvas.create_rectangle(
Saint-maur-des-fosses= canvas.create_rectangle(
Nanterre= canvas.create_rectangle(



canvas.create_image(0, 0, anchor=NW, image=PhotoIDF)






    
#Lancerment du programme
canvas.pack()

Pageprincipale.mainloop()
