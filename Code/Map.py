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



canvas.create_image(0, 0, anchor=NW, image=PhotoIDF)






    
#Lancerment du programme
canvas.pack()

Pageprincipale.mainloop()
