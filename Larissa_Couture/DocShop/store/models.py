from django.db import models
from django.urls import reverse


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
