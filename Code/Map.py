from tkinter import*
import random
import copy
import time

#Page
Pageprincipale = Tk()
Pageprincipale.geometry ("1200x900+65+50")
Pageprincipale.title('Carte McDo/Quick')
Pageprincipale.maxsize (width=728,height=589)
Pageprincipale.minsize (width=728,height=589)
Pageprincipale['bg']='Black'



#photo
PhotoIDF = PhotoImage(file="CIDF.png")

#Fond
canvas = Canvas(Pageprincipale,width=728, height=589)


#Création des villes:


Paris1_coords = (309,206,310,207)
Paris1 = canvas.create_rectangle(*Paris1_coords)

Paris2_coords = (309,204,310,205)
Paris2 = canvas.create_rectangle(*Paris2_coords)

Paris3_coords = (311,204,312,205)
Paris3 = canvas.create_rectangle(*Paris3_coords)

Paris4_coords = (311,206,312,210)
Paris4 = canvas.create_rectangle(*Paris4_coords)

Paris5_coords = (310,211,312,213)
Paris5 = canvas.create_rectangle(*Paris5_coords)

Paris6_coords = (309,209,310,213)
Paris6 = canvas.create_rectangle(*Paris6_coords)

Paris7_coords = (290,203,302,208)
Paris7 = canvas.create_rectangle(*Paris7_coords)

Paris8_coords = (290,198,298,202)
Paris8 = canvas.create_rectangle(*Paris8_coords)

Paris9_coords = (299,198,309,201)
Paris9 = canvas.create_rectangle(*Paris9_coords)

Paris10_coords = (309,198,315,201)
Paris10 = canvas.create_rectangle(*Paris10_coords)

Paris11_coords = (313,200,322,208)
Paris11 = canvas.create_rectangle(*Paris11_coords)

Paris12_coords = (317,215,345,220)
Paris12 = canvas.create_rectangle(*Paris12_coords)

Paris13_coords = (311,215,318,225)
Paris13 = canvas.create_rectangle(*Paris13_coords)

Paris14_coords = (305,215,311,225)
Paris14 = canvas.create_rectangle(*Paris14_coords)

#Paris15_coords = (282,213,295,223)
#Paris15 = canvas.create_rectangle(*Paris15_coords)

Paris16_coords = (275,200,282,223)
Paris16 = canvas.create_rectangle(*Paris16_coords)

Paris17_coords = (290,185,303,193)
Paris17 = canvas.create_rectangle(*Paris17_coords)

Paris18_coords = (303,185,312,193)
Paris18 = canvas.create_rectangle(*Paris18_coords)

Paris19_coords = (313,185,322,195)
Paris19 = canvas.create_rectangle(*Paris19_coords)

Paris20_coords = (325,200,330,208)
Paris20 = canvas.create_rectangle(*Paris20_coords)

StDenis_coords = (308,162,311,183)
StDenis = canvas.create_rectangle(*StDenis_coords)

BoulogneBilancourt_coords = (268,211,275,220)
BoulogneBilancourt = canvas.create_rectangle(*BoulogneBilancourt_coords)

Versailles_coords = (235,230,250,240)
Versailles = canvas.create_rectangle(*Versailles_coords)

Creteil_coords = (335,230,345,240)
Creteil = canvas.create_rectangle(*Creteil_coords)

NeuillySurSeine_coords = (280,185,290,190)
NeuillySurSeine = canvas.create_rectangle(*NeuillySurSeine_coords)

Cergy_coords = (202,115,220,125)
Cergy = canvas.create_rectangle(*Cergy_coords)

Rambouillet_coords = (145,350,155,355)
Rambouillet = canvas.create_rectangle(*Rambouillet_coords)

Meaux_coords = (485,150,500,165)
Meaux= canvas.create_rectangle(*Meaux_coords)

Evry_coords = (330,305,340,320)
Evry= canvas.create_rectangle(*Evry_coords)

Orsay_coords = (250,270,255,275)
Orsay= canvas.create_rectangle(*Orsay_coords)

Melun_coords = (405,360,415,370)
Melun= canvas.create_rectangle(*Melun_coords)

Etampes_coords = (175,415,190,425)
Etampes= canvas.create_rectangle(*Etampes_coords)

Goussainville_coords = (360,125,365,130)
Goussainville= canvas.create_rectangle(*Goussainville_coords)

poissy_coords = (197,160,207,175)
Poissy = canvas.create_rectangle(*poissy_coords)

Villepinte_coords = (365,145,375,150)
Villepinte= canvas.create_rectangle(*Villepinte_coords)

Coulommiers_coords=(520,240,550,245)
Coulommiers= canvas.create_rectangle(*Coulommiers_coords)

ClayeSouilly_coords = (420,160,435,170)
ClayeSouilly= canvas.create_rectangle(*ClayeSouilly_coords)

BrieComteRobert_coords = (385,280,390,290)
BrieComteRobert= canvas.create_rectangle(*BrieComteRobert_coords)

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

LaFertesousJouarre_coords = (565,150,575,160)
LaFertesousJouarre= canvas.create_rectangle(*LaFertesousJouarre_coords)

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

VillierssurMarne_coords = (367,220,377,225)
VillierssurMarne= canvas.create_rectangle( *VillierssurMarne_coords)

Torcy_coords = (405,200,415,210)
Torcy = canvas.create_rectangle(*Torcy_coords)

Plaisir_coords = (170,225,185,240)
Plaisir = canvas.create_rectangle(*Plaisir_coords)

Palaiseau_coords = (255,270,265,280)
Palaiseau = canvas.create_rectangle(*Palaiseau_coords)

ManteslaJolie_coords = (90,130,100,140)  
ManteslaJolie = canvas.create_rectangle(*ManteslaJolie_coords)

Sarcelles_coords = (310,140,320,150)
Sarcelles= canvas.create_rectangle(*Sarcelles_coords)

LePerrayenYvelines_coords = (130,305,140,315)
LePerrayenYvelines= canvas.create_rectangle(*LePerrayenYvelines_coords)

DammartinenGoele_coords = (415,100,425,110)
DammartinenGoele= canvas.create_rectangle(*DammartinenGoele_coords)

Serris_coords = (440,205,450,215)
Serris = canvas.create_rectangle(*Serris_coords)

Bombon_coords = (425,355,435,365)
Bombon= canvas.create_rectangle(*Bombon_coords)

Bretignysurorge_coords = (300,320,310,330)
Bretignysurorge= canvas.create_rectangle(*Bretignysurorge_coords)

Avon_coords = (430,420,440,430)
Avon= canvas.create_rectangle(*Avon_coords)

Saintmaurdesfosses_coords = (350,230,360,240)
Saintmaurdesfosses= canvas.create_rectangle(*Saintmaurdesfosses_coords)


Nanterre_coords = (250,180,270,200)
Nanterre= canvas.create_rectangle(*Nanterre_coords)

canvas.create_image(0, 0, anchor=NW, image=PhotoIDF)



coords = [Paris1_coords, Paris2_coords, Paris3_coords, Paris4_coords, Paris5_coords, Paris6_coords, Paris7_coords, Paris8_coords, Paris9_coords, Paris10_coords, Paris11_coords, Paris12_coords, Paris13_coords, Paris14_coords,  Paris16_coords, Paris17_coords, Paris18_coords, Paris19_coords,Paris20_coords, StDenis_coords, BoulogneBilancourt_coords, Versailles_coords,Creteil_coords, NeuillySurSeine_coords, Cergy_coords, Rambouillet_coords, Meaux_coords, Evry_coords, Orsay_coords, Melun_coords, Etampes_coords, Goussainville_coords, poissy_coords, Villepinte_coords, Coulommiers_coords, ClayeSouilly_coords, BrieComteRobert_coords, Dourdan_coords, GretzArmainvilliers_coords, Thoiry_coords, LIsleAdam_coords, MagnyenVexin_coords, LesMureaux_coords, Limay_coords, MontereauFaultYonne_coords, Provins_coords, Nemours_coords, Guyancourt_coords, Elancourt_coords, Chessy_coords, Nangis_coords, IssylesMoulineaux_coords, LaFertesousJouarre_coords, Noisylegrand_coords, SaintGermainenLaye_coords, LaCellesaintCloud_coords, RosnysousBois_coords, Franconville_coords, Gonesse_coords, VillierssurMarne_coords, Torcy_coords, Plaisir_coords, Palaiseau_coords, ManteslaJolie_coords, Sarcelles_coords, LePerrayenYvelines_coords, DammartinenGoele_coords, Serris_coords, Bombon_coords, Bretignysurorge_coords, Avon_coords, Saintmaurdesfosses_coords, Nanterre_coords]

Villes = [(Paris1, "Paris1"), (Paris2,"Paris2"), (Paris3,"Paris3"), (Paris4,"Paris4"), (Paris5,"Paris5"), (Paris6,"Paris6"), (Paris7,"Paris7"), (Paris8,"Paris8"), (Paris9,"Paris9"), (Paris10,"Paris10"), (Paris11,"Paris11"), (Paris12,"Paris12"),  (Paris13,"Paris13"), (Paris14,"Paris14"),  (Paris16,"Paris16"), (Paris17,"Paris17"), (Paris18,"Paris18"), (Paris19,"Paris19"), (Paris20,"Paris20"), (StDenis,"Saint-Denis"), (BoulogneBilancourt,"Boulogne-Billancourt"), (Versailles,"Versailles"), (Creteil,"Creteil"), (NeuillySurSeine,"Neuilly-Sur-Seine"), (Cergy,"Cergy"), (Rambouillet,"Rambouillet"),( Meaux,"Meaux"), (Evry,"Evry"), (Orsay,"Orsay"), (Melun,"Melun"), (Etampes,"Etampes"), (Goussainville,"Goussainville"), (Poissy,"Poissy"), (Villepinte,"Villepinte"), (Coulommiers,"Coulommiers"), (ClayeSouilly,"Claye-Souilly"), (BrieComteRobert,"Brie-Comte-Robert"), (Dourdan,"Dourdan"), (GretzArmainvilliers,"Gretz-Armainvilliers"), (Thoiry,"Thoiry"), (LIsleAdam,"L’Isle-Adam"), (MagnyenVexin,"Magny-en-Vexin"), (LesMureaux,"Les Mureaux"), (Limay,"Limay"), (MontereauFaultYonne,"Montereau-Fault-Yonne"), (Provins,"Provins"), (Nemours,"Nemours"), (Guyancourt,"Guyancourt"), (Elancourt,"Elancourt"), (Chessy,"Chessy"), (Nangis,"Nangis"), (IssylesMoulineaux,"Issy-les-Moulineux"), (LaFertesousJouarre,"La Ferté-sous-Jouarre"), (Noisylegrand,"Noisy-le-grand"), (SaintGermainenLaye,"Saint-Germain-en-Laye"), (LaCellesaintCloud,"La Celle-saint-Cloud"), (RosnysousBois,"Rosny-sous-Bois"), (Franconville,"Franconville"), (Gonesse,"Gonesse"), (VillierssurMarne,"Villiers-sur-Marne"), (Torcy,"Torcy"), (Plaisir,"Plaisir"), (Palaiseau,"Palaiseau"), (ManteslaJolie,"Mantes-la-Jolie"), (Sarcelles,"Sarcelles"), (LePerrayenYvelines,"Le Perray-en-Yvelines"), (DammartinenGoele,"Dammartin-en-Goele"), (Serris,"Serris"), (Bombon,"Bombon"), (Bretignysurorge,"Bretigny-sur-orge"), (Avon,"Avon"), (Saintmaurdesfosses,"Saint-maur-des-fosses"), (Nanterre,"Nanterre")]





def rectangle(ListeDictMcDo,ListeDictQuick):#,SauvegardeDictionnaireMcDo,SauvegardeDictionnaireQuick
    
    
    
    for j in range(1,len(ListeDictMcDo)):
        canvas.create_image(0, 0, anchor=NW, image=PhotoIDF)
        DictMcDo = ListeDictMcDo[j]
        DictQuick = ListeDictQuick[j]
        for i in range(len(Villes)):
            
            xhaut, yhaut, xbas, ybas = coords[i]
            #for h  in DictMcDo:
            
            nomVille = Villes[i][1]
            h = int(DictMcDo[nomVille])
            #a = SauvegardeDictionnaireMcDo[nomVille]
           
                #print(xhaut, yhaut, xbas, ybas, coords[i])    
            #if a!=h: #DictMcDo[h] != SauvegardeDictionnaireMcDo[h]:
               # for j in range(a,h):
           # if int(SauvegardeDictionnaireMcDo[nomVille])!=int(DictMcDo[nomVille]):
            f#or a in range(int(SauvegardeDictionnaireMcDo[nomVille]),int(DictMcDo[nomVille])):
            if h!=0:
                Emplacementx=(xhaut+xbas)/2+2
                Emplacementy=(yhaut+ybas)/2+2
                
                canvas.create_rectangle(Emplacementx, Emplacementy, Emplacementx+5, Emplacementy+5,fill = "yellow")
                if h > 1:
                    canvas.create_text(Emplacementx, Emplacementy,text=h,fill = 'yellow')
                        
            nomVille2 = Villes[i][1]
            p = int(DictQuick[nomVille2])
                    #for k  in DictQuick:        
                #if  DictQuick[k] != SauvegardeDictionnaireQuick[k]:
            #if int(SauvegardeDictionnaireQuick[nomVille])!=int(DictQuick[nomVille]):
                #for a in range(int(SauvegardeDictionnaireQuick[nomVille]),int(DictQuick[nomVille])):
            if p!= 0:
            
                        #for j in range(SauvegardeDictionnaireQuick[k],DictQuick[k]):
            
                Emplacementx=(xhaut+xbas)/2-2
                Emplacementy=(yhaut+ybas)/2-2
                canvas.create_rectangle(Emplacementx, Emplacementy, Emplacementx+5, Emplacementy+5, fill = "red")    
                
                if p > 1:
                    canvas.create_text(Emplacementx, Emplacementy,text=p,fill = 'red')
                
            
            
            
            #SauvegardeDictionnaireMcDo = DictMcDo
        
            #SauvegardeDictionnaireQuick = DictQuick
           
            #rectangle(ListeDictMcDo,ListeDictQuick,DictMcDo,DictQuick)

            
            
DictMcDo = dict()
DictQuick = dict()
ListeDictMcDo = []
ListeDictQuick = []
temp = dict()
f = open("map.txt")
liste_lignes = f.readlines()
        
f.close()
 
# creation d'un point rouge pour un mc do et d'un point vert pour un quick
#DictMcDo = {'Paris15':0,'Saint-Denis': 5, 'Paris19': 1, 'Paris5': 1, 'Plaisir': 0, 'Paris4': 0, 'Paris1': 0, 'Etampes': 1, 'Paris18': 0, 'Thoiry': 0, 'Dourdan': 0, 'Claye-Souilly': 0, 'Magny-en-Vexin': 0, 'Gonesse': 0, 'Paris3': 0, 'Poissy': 0, 'Nangis': 0, 'Les Mureaux': 0, 'Melun': 0, 'Meaux': 0, 'Brie-Comte-Robert': 0, 'Paris13': 0, 'Paris17': 0, 'Paris16': 0, 'Paris20': 0, 'Villiers-sur-Marne': 0, 'Paris6': 0, 'Coulommiers': 0, 'Serris': 0, 'Limay': 0, 'Gretz-Armainvilliers': 0, 'Versailles': 0, 'La Celle-saint-Cloud': 0, 'Palaiseau': 0, 'Boulogne-Billancourt': 0, 'Villepinte': 0, 'Noisy-le-grand': 0, 'Chessy': 0, 'Saint-Germain-en-Laye': 0, 'Avon': 0, 'Nemours': 0, 'Bombon': 0, 'Franconville': 0, 'Paris10': 0, 'Goussainville': 0, 'Rambouillet': 0, 'Paris8': 0, 'Paris11': 0, 'Cergy': 0, 'Le Perray-en-Yvelines': 0, 'Guyancourt': 0, 'Paris7': 0, 'Montereau-Fault-Yonne': 0, 'Paris2': 0, 'La Ferté-sous-Jouarre': 0, 'Rosny-sous-Bois': 0, 'Provins': 0, 'Neuilly-Sur-Seine': 0, 'Paris14': 0, 'Dammartin-en-Goele': 0, 'Paris12': 0, 'Orsay': 0, 'Saint-maur-des-fosses': 0, 'Creteil': 0, 'Elancourt': 0, 'Torcy': 0, 'Evry': 0, 'Sarcelles': 0, 'Bretigny-sur-orge': 0, 'Mantes-la-Jolie': 0, 'Issy-les-Moulineux': 0, 'L’Isle-Adam': 0, 'Nanterre': 0, 'Paris9': 0}


#DictQuick = {'Paris15':0,'Saint-Denis': 5, 'Paris19': 0, 'Paris5': 0, 'Plaisir': 0, 'Paris4': 0, 'Paris1': 0, 'Etampes': 0, 'Paris18': 0, 'Thoiry': 0, 'Dourdan': 0, 'Claye-Souilly': 0, 'Magny-en-Vexin': 0, 'Gonesse': 0, 'Paris3': 0, 'Poissy': 0, 'Nangis': 0, 'Les Mureaux': 0, 'Melun': 0, 'Meaux': 0, 'Brie-Comte-Robert': 0, 'Paris13': 0, 'Paris17': 0, 'Paris16': 0, 'Paris20': 0, 'Villiers-sur-Marne': 0, 'Paris6': 0, 'Coulommiers': 0, 'Serris': 0, 'Limay': 0, 'Gretz-Armainvilliers': 0, 'Versailles': 0, 'La Celle-saint-Cloud': 0, 'Palaiseau': 0, 'Boulogne-Billancourt': 0, 'Villepinte': 0, 'Noisy-le-grand': 0, 'Chessy': 0, 'Saint-Germain-en-Laye': 0, 'Avon': 0, 'Nemours': 0, 'Bombon': 0, 'Franconville': 0, 'Paris10': 0, 'Goussainville': 0, 'Rambouillet': 0, 'Paris8': 0, 'Paris11': 0, 'Cergy': 0, 'Le Perray-en-Yvelines': 0, 'Guyancourt': 0, 'Paris7': 0, 'Montereau-Fault-Yonne': 0, 'Paris2': 0, 'La Ferté-sous-Jouarre': 0, 'Rosny-sous-Bois': 0, 'Provins': 0, 'Neuilly-Sur-Seine': 0, 'Paris14': 0, 'Dammartin-en-Goele': 0, 'Paris12': 0, 'Orsay': 1, 'Saint-maur-des-fosses': 0, 'Creteil': 2, 'Elancourt': 0, 'Torcy': 0, 'Evry': 0, 'Sarcelles': 0, 'Bretigny-sur-orge': 3, 'Mantes-la-Jolie': 0, 'Issy-les-Moulineux': 0, 'L’Isle-Adam': 0, 'Nanterre': 0, 'Paris9': 0}

#SauvegardeDictionnaireMcDo = {'Paris15':0,'Saint-Denis': 0, 'Paris19': 0, 'Paris5': 0, 'Plaisir': 0, 'Paris4': 0, 'Paris1': 0, 'Etampes': 0, 'Paris18': 0, 'Thoiry': 0, 'Dourdan': 0, 'Claye-Souilly': 0, 'Magny-en-Vexin': 0, 'Gonesse': 0, 'Paris3': 0, 'Poissy': 0, 'Nangis': 0, 'Les Mureaux': 0, 'Melun': 0, 'Meaux': 0, 'Brie-Comte-Robert': 0, 'Paris13': 0, 'Paris17': 0, 'Paris16': 0, 'Paris20': 0, 'Villiers-sur-Marne': 0, 'Paris6': 0, 'Coulommiers': 0, 'Serris': 0, 'Limay': 0, 'Gretz-Armainvilliers': 0, 'Versailles': 0, 'La Celle-saint-Cloud': 0, 'Palaiseau': 0, 'Boulogne-Billancourt': 0, 'Villepinte': 0, 'Noisy-le-grand': 0, 'Chessy': 0, 'Saint-Germain-en-Laye': 0, 'Avon': 0, 'Nemours': 0, 'Bombon': 0, 'Franconville': 0, 'Paris10': 0, 'Goussainville': 0, 'Rambouillet': 0, 'Paris8': 0, 'Paris11': 0, 'Cergy': 0, 'Le Perray-en-Yvelines': 0, 'Guyancourt': 0, 'Paris7': 0, 'Montereau-Fault-Yonne': 0, 'Paris2': 0, 'La Ferté-sous-Jouarre': 0, 'Rosny-sous-Bois': 0, 'Provins': 0, 'Neuilly-Sur-Seine': 0, 'Paris14': 0, 'Dammartin-en-Goele': 0, 'Paris12': 0, 'Orsay': 0, 'Saint-maur-des-fosses': 0, 'Creteil': 0, 'Elancourt': 0, 'Torcy': 0, 'Evry': 0, 'Sarcelles': 0, 'Bretigny-sur-orge': 0, 'Mantes-la-Jolie': 0, 'Issy-les-Moulineux': 0, 'L’Isle-Adam': 0, 'Nanterre': 0, 'Paris9': 0}


#SauvegardeDictionnaireQuick = {'Paris15':0,'Saint-Denis': 0, 'Paris19': 0, 'Paris5': 0, 'Plaisir': 0, 'Paris4': 0, 'Paris1': 0, 'Etampes': 0, 'Paris18': 0, 'Thoiry': 0, 'Dourdan': 0, 'Claye-Souilly': 0, 'Magny-en-Vexin': 0, 'Gonesse': 0, 'Paris3': 0, 'Poissy': 0, 'Nangis': 0, 'Les Mureaux': 0, 'Melun': 0, 'Meaux': 0, 'Brie-Comte-Robert': 0, 'Paris13': 0, 'Paris17': 0, 'Paris16': 0, 'Paris20': 0, 'Villiers-sur-Marne': 0, 'Paris6': 0, 'Coulommiers': 0, 'Serris': 0, 'Limay': 0, 'Gretz-Armainvilliers': 0, 'Versailles': 0, 'La Celle-saint-Cloud': 0, 'Palaiseau': 0, 'Boulogne-Billancourt': 0, 'Villepinte': 0, 'Noisy-le-grand': 0, 'Chessy': 0, 'Saint-Germain-en-Laye': 0, 'Avon': 0, 'Nemours': 0, 'Bombon': 0, 'Franconville': 0, 'Paris10': 0, 'Goussainville': 0, 'Rambouillet': 0, 'Paris8': 0, 'Paris11': 0, 'Cergy': 0, 'Le Perray-en-Yvelines': 0, 'Guyancourt': 0, 'Paris7': 0, 'Montereau-Fault-Yonne': 0, 'Paris2': 0, 'La Ferté-sous-Jouarre': 0, 'Rosny-sous-Bois': 0, 'Provins': 0, 'Neuilly-Sur-Seine': 0, 'Paris14': 0, 'Dammartin-en-Goele': 0, 'Paris12': 0, 'Orsay': 0, 'Saint-maur-des-fosses': 0, 'Creteil': 0, 'Elancourt': 0, 'Torcy': 0, 'Evry': 0, 'Sarcelles': 0, 'Bretigny-sur-orge': 0, 'Mantes-la-Jolie': 0, 'Issy-les-Moulineux': 0, 'L’Isle-Adam': 0, 'Nanterre': 0, 'Paris9': 0}

def lire_mois(lignes):
    dic_mc_dos = {}
    dic_quicks = {}
    for l in lignes:
        if l.startswith("#"):
            break
        nom,mcdos,quicks = l.split(",")
        dic_mc_dos[nom] = int(mcdos)
        dic_quicks[nom] = int(quicks)
    return dic_mc_dos,dic_quicks
            
#Lancerment du programme
canvas.pack()
liste_lignes = iter(liste_lignes)
next(liste_lignes)

#SauvegardeDictionnaireQuick=dict()
#SauvegardeDictionnaireMcDo=dict()
while True:
    
    DictMcDo,DictQuick = lire_mois(liste_lignes)
    ListeDictMcDo.append(DictMcDo)
    ListeDictQuick.append(DictQuick)  
    rectangle(ListeDictMcDo,ListeDictQuick)#,SauvegardeDictionnaireMcDo,SauvegardeDictionnaireQuick
    #SauvegardeDictionnaireQuick=DictMcDo
    #SauvegardeDictionnaireMcDo=DictQuick
    Pageprincipale.update_idletasks()
    Pageprincipale.update()
    print(ListeDictMcDo)
    time.sleep(2)
    
    
    
