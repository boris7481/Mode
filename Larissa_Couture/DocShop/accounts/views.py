from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

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
    # la fonction login permet de lioer la requette au user creer
    return render(request, 'accounts/signup.html')

    # request.POST est un dictionaire dont les clefs username et password defini dans le fichier signu.html
    # La fonction login te permet de connecter L#l'utilisateur


def login_user(request):
    if request.method == "POST":
        # Connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')
