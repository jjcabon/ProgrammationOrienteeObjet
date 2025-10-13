class ClasseDeLycee:
    nom = "terminale"
    numero = 1 
    #liste des élèves
    eleves = [] # ce sont les attributs
    def ajoute_eleve(self, eleve1):
        self.eleves.append(eleve1)
    #méthode
    def __init__(self,nom = "Terminale",numero = 1,eleves = []):
        self.nom = nom
        self.numero = numero
        self.eleves
    def __str__(self):
        return f"Classede{self.nom}{self.numero}avec des eleves{self.eleves}"
    
    
term1= ClasseDeLycee()
term2= ClasseDeLycee() # instance's d'objet
print(term1.nom)
print(term2.numero)
print(term2.eleves)
term2.numero = 2
seconde2 = ClasseDeLycee()
seconde2.nom = "seconde"
seconde2.numero = 2
term1.ajoute_eleve("Alan Turing")
print(term1.eleves)
term2.ajoute_eleve(["Turing", "Alan","machine de Turing",1936])
print(term2.eleves) 
print(term2.eleves[1][3])
seconde1 = ClasseDeLycee("seconde", 1, ["Lovelace","Ada","Concevoir des programmes",1842])
print(seconde1.nom)
print(seconde1.eleves)
print(seconde1.eleves[1][3])
print(term1)
print(seconde1)