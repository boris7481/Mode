from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

# cette fonction get_user_model nous permet de recuprer un object qui correspond a notre model d 'utilisateur

User = get_user_model() # je dois inpecter cette fonction pour comprendre ce qu elle fait


def signup(request):
    if request.method == "POST":
        # Traiter le formulaire
        # le username et le password ici sont ceux qui sont definis dans le formulaire du signup.html
        # c est pouquoi on doit les mettre ici comme cles car la fonction get retourne un dictionaire
        username = request.POST.get("username") # ici on recupere le nom que le user va entrer dans le formulaire
        password = request.POST.get("password") # ici on recupere le password que le user va entrer dans le formulaire
        user = User.objects.create_user(username=username,
                                        password=password) # ici on cree un user et on lui
                                                            # passe les infos recuperer au niveau du formulaire
        login(request, user)
        return redirect("index")
    # la fonction login permet de lioer la requette au user creer
    return render(request, 'accounts/signup.html')

    # request.POST est un dictionaire dont les clefs username et password defini dans le fichier signu.html
    # La fonction login te permet de connecter L#l'utilisateur


def login_user(request):
    if request.method == "POST":
        # Connecter l'utilisateur
        username = request.POST.get("username") # ici on recupere le nom que le user va entrer dans le formulaire
        password = request.POST.get("password") # ici on recupere le password que le user va entrer dans le formulaire

        user = authenticate(username=username, password=password)
        if user: # au cas ou le user existe on le connecte
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html')


def logout_user(request): # cette methode permet de deconnecter le suer et de rediriger vers la vue d'index
    logout(request)
    return redirect('index')
