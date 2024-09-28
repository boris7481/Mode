from django.contrib import admin
from store.models import Product, Order, Cart

admin.site.register(Product)  # on dit a django d'afficher nos produite a l'interieur de l interface d'admin
admin.site.register(Order)  # # on dit a django d'afficher nos Order a l'interieur de l interface d'admin
admin.site.register(Cart)  # on dit a django d'afficher nos Cart a l'interieur de l interface d'admin
