from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

# cette fonction get_user_model nous permet de recuprer un object qui correspond a notre model d 'utilisateur

User = get_user_model()


def signup(request):
    return render(request, 'accounts/signup.html')

    # request.POST est un dictionaire donct les clefs username et password defini dans le fichier signu.html
    # La fonction login te permet de connecter L#utlisateur


