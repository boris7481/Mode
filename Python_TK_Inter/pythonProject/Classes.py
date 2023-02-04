

class Humain:
    lieu_habitation = "terre" # ici on a une methode de classe cad qu elle n,est pas lier a une instance de classe comme H1
    def __ini__(self, nom , age):# ici on cree une une classe
        self.non = nom
        self.age = age

    def parler(self, message):# ici on cree une methode self = methode standard
        print("{} a dit {}".format( self ,  message)) # verifier aussi la ligne ci encor

    def changer_planete(cls, nouvelle_planete):#  cls methode de classe
        Humain.lieu_habitation = nouvelle_planete

    changer_planete = classmethod(changer_planete)
    # cette ligne est tres importante il n est pas definit dans la methode de classe mais dnas la classe

    def definition(): # Ce ci est une methode statique NB elle est definit dans la classe Humain
        print("je suis entrain d apprendre a programmer")

    definition = staticmethod(definition) # C est une methode independante

# parler est une methode distance Cad qu il faut creer un object avant de l utiliser dessus


print(Humain.lieu_habitation)
# H2 = Humain("junior" , 20)  # TypeError: Humain() takes no arguments voila un truc a verifier
# print(H2)


H1 = Humain()  # la partie ci a revoir
print(H1)
H1.parler("bonjour a tous")
H1.parler("coment vas tu ? :")
Humain.changer_planete("mars")

print("planete actuelle : {}".format(Humain.lieu_habitation))

Humain.definition()
