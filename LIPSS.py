prixEuro = 4924

prixEuro*24000
118152000
Ariary = prixEuro*24000
#print(Ariary)

#-------------------------------------------------------------

masse = 1200
vitesse = 15000

Ec = (1/2)*masse*((vitesse)**2)

#print("Energie Cinetique = ",Ec)

#-------------------------------------------------------------

H = 80
B = 150
h = 20
b = (h*B)/H
#print("base = ",b)

S = (H*B)/2 - (h*b)/2
#print("Surface = ",S)

#-------------------------------------------------------------

pi =  3.14

r= (S/pi)**0.5
#print("rayon du cercle = ",r)


#-------------------------------------------------------------
# Calcul rapport d'un surface :
c = 1  #cote = 1 m²
S = c**2  #Grand surface du carré 
S10 = (c*((1/2)**10))**2  #Surface 1/10 

rapport = (S10/S)*100

print("Rapport de surface = ", rapport)


