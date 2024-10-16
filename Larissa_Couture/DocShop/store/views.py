from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from store.models import Product, Cart, Order


def index(request):
    products = Product.objects.all()  # ici on a un querset a cause de la methode all()
    return render(request, 'store/index.html', context={"products": products})


# ce chemin ci 'store/index.html' est pris a partir du dossier templates

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "store/detail.html", context={"product": product})


# ce chemin ci 'store/detail.html' est pris a partir du dossier templates
# tous le code  de la vue add_to_cart ci dessous te permet de gerer de maniere plus efficasse le panier
# gestion du user selon qu'il a deja un panier ou pas
# si le user a deja un article dans le panier on increment l'article de 1

def add_to_cart(request, slug):
    user = request.user  # recuperation du user ici
    product = get_object_or_404(Product, slug=slug)
    # recuperation du produit et du slug passe au niveau de L'URL
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,
                                                 ordered=False,  # nous permet de cibler le bonne element
                                                 product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
# get_object_or_404 permet de recuperer un objet s 'il existe , au cas contraire on retourne une page d'erreur
    return render(request, 'store/cart.html', context={"orders": cart.orders.all()})


# ce chemin ci 'store/cart.html' est pris a partir du dossier templates

def delete_cart(request):
    cart = request.user.cart
    if cart:
        cart.delete()

    return redirect("index")
