from django.contrib import admin

from accounts.models import Shopper

admin.site.register(Shopper)

# dans la ligne ci dessous on enregistre notre nouveau modele d'utilisateur que l'on a creer
# dans notre system d'administration de django
