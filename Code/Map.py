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
Rambouillet = canvas.create_rectangle(145,350,155,355)
Meaux= canvas.create_rectangle(485,150,500,165)
Evry= canvas.create_rectangle(330,305,340,320)
Orsay= canvas.create_rectangle(250,270,255,275)
Melun= canvas.create_rectangle(405,360,415,370)
Etampes= canvas.create_rectangle(175,415,190,425)
Goussainville= canvas.create_rectangle(360,125,365,130)

poissy_coords = (197,160,207,175)
Poissy = canvas.create_rectangle(*poissy_coords)

Villepinte_coords = (365,145,375,150)
Villepinte= canvas.create_rectangle(*Villepinte_coords)

Coulommiers_coords=(520,240,550,245)
Coulommiers= canvas.create_rectangle(*Coulommiers_coords)

ClayeSouilly= canvas.create_rectangle(420,160,435,170)
BrieComteRobert= canvas.create_rectangle(385,280,390,290)

Dourdan_coords = (170,356,185,366)
Dourdan= canvas.create_rectangle(*Dourdan_coords)

GretzArmainvilliers_coords = (430,250,435,260)
GretzArmainvilliers= canvas.create_rectangle(*GretzArmainvilliers_coords)

Thoiry_coords = (115,205,125,215)
Thoiry= canvas.create_rectangle(*Thoiry_coords)

LIsleAdam_coords = (262,73,275,83)
LIsleAdam = canvas.create_rectangle(*LIsleAdam_coords)

MagnyenVexin_coords = (120,45,125,50)
MagnyenVexin = canvas.create_rectangle(*MagnyenVexin_coords)

LesMureaux_coords = (170,135,180,145)
LesMureaux= canvas.create_rectangle(*LesMureaux_coords)

Limay_coords = (105,135,115,145)
Limay= canvas.create_rectangle(*Limay_coords)

MontereauFaultYonne_coords = (505,435,515,445)
MontereauFaultYonne = canvas.create_rectangle(*MontereauFaultYonne_coords)

Provins_coords = (610,375,620,385)
Provins= canvas.create_rectangle(*Provins_coords)

Nemours_coords = (420,470,430,480)
Nemours= canvas.create_rectangle(*Nemours_coords)

Guyancourt_coords = (220,250,230,260)
Guyancourt = canvas.create_rectangle(*Guyancourt_coords)

Elancourt_coords = (180,237,190,247)
Elancourt= canvas.create_rectangle(*Elancourt_coords)

Chessy_coords = (445,190,455,200)
Chessy= canvas.create_rectangle(*Chessy_coords)

Nangis_coords = (540,370,550,380)
Nangis= canvas.create_rectangle(*Nangis_coords)

IssylesMoulineaux_coords = (272,217,285,225)
IssylesMoulineaux = canvas.create_rectangle(*IssylesMoulineaux_coords)

LaFertésousJouarre_coords = (565,150,575,160)
LaFertésousJouarre= canvas.create_rectangle(*LaFertésousJouarre_coords)

Noisylegrand_coords = (370,205,380,220)
Noisylegrand = canvas.create_rectangle(*Noisylegrand_coords)

SaintGermainenLaye_coords = (220,140,240,180)
SaintGermainenLaye= canvas.create_rectangle(*SaintGermainenLaye_coords)

LaCellesaintCloud_coords = (235,211,250,220)
LaCellesaintCloud= canvas.create_rectangle(*LaCellesaintCloud_coords)

RosnysousBois_coords = (348,195,355,203)
RosnysousBois= canvas.create_rectangle(*RosnysousBois_coords)

Franconville_coords = (255,145,268,155)
Franconville = canvas.create_rectangle(*Franconville_coords)

Gonesse_coords = (350,140,360,150)
Gonesse= canvas.create_rectangle(*Gonesse_coords)






canvas.create_image(0, 0, anchor=NW, image=PhotoIDF)








"""Villiers-sur-Marne= canvas.create_rectangle(
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
Nanterre= canvas.create_rectangle("""



    
#Lancerment du programme
canvas.pack()

Pageprincipale.mainloop()
