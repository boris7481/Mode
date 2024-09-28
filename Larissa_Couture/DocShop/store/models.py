from django.db import models
from django.urls import reverse
from django.utils import timezone

from shop.settings import AUTH_USER_MODEL


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)  # on l'a ajouter apres quelquwes videos mais on peut le rajouter des le
    # depart l orsqu'on cree le model
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.name

    # cette methode dois obligatoirement s'appelle comme cela permet de gerer les urls aui niveau de l'administrtion
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


# Articles
"""
- Utilisateur
- Produit
- Quantite
- Commande ou nom
"""


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} {self.quantity}"


# Panier
"""
- Utilisateur
- Articles
- commande ou nom
- Date de la commande
"""


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        # on surchage la methode delete pour pouvoir supprimer un panier a partir du system d amin
        for order in self.orders.all():  # on boucle sur tous les articles attachees au panier
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()  # on sauvegarde le model

        self.orders.clear()  # permet de detacher les elements permet de casser la relation entre article et panier
        # du ManyToManyField. Les articles ne seront plus lies a notre panier
        super().delete(*args, **kwargs)
