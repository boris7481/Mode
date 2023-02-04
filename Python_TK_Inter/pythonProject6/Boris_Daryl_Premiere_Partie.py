import random

with open("Boris.txt", "r") as file:
    data = file.read()
    data_into_list = data.split("\n")
print(data_into_list)

data_filter = []
for name in data_into_list:
   if name not in data_filter:
        data_filter.append(name)


print(data_filter)

class Player:
    def __init__(self , name): # ici j ai juste besoin du nom de mon objet
        self.name = name
        self.puissance = random.randint(10,260)
        self.resistance =  random.randint(10,260)
    def info(self): # ce ci est ne methode de la classe Player
        print("{} a une puissance de {}  et une resistance de {}".format(       self.name, self.puissance , self.resistance ) )

listplayer = []
for name in data_filter:
    listplayer.append(Player(name))   # j ai ici une liste rempli d objet
listplayer[4].info()                  # j applique la methode a chaque objet selectionner

print(listplayer)

with open("Player.txt", "w") as fichier:
    for item in listplayer:
        fichier.write("%s\n" % item.name)
#    for text in listplayer:
#        listplayer.append(Player(text))
#   record_1 = fichier.write(text[0])
#    record = fichier.write("boris daryl 20\n")
#    record = fichier.write("boris daryl 30\n")
print(fichier)
print(fichier.name)

# Procedure d identification
check  = False
username = input("Enter username: ")
for user in data_filter:
    if user == username:
        check = True
        print("Username is: " + username)
if check == False:
     print("please try angai")


