from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login

# cette fonction get_user_model nous permet de recuprer un object qui correspond a notre model d 'utilisateur

User = get_user_model()


def signup(request):
    if request.method == "POST":
        # Traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                        password=password)
        login(request, user)
        return redirect("index")
# la fonction login permet de leir la requette au user creer
    return render(request, 'accounts/signup.html')

    # request.POST est un dictionaire donct les clefs username et password defini dans le fichier signu.html
    # La fonction login te permet de connecter L#utlisateur
