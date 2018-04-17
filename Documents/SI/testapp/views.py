from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.forms import ModelForm
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import auth


# Create your views here.
from django.template.context_processors import csrf
from django.views.generic import FormView

from testapp.models import Personne, Etudiant, Groupe


class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'


class GroupeForm(ModelForm):
    class Meta:
        model = Groupe
        fields = '__all__'

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

def home(request):
    personne = Personne.objects.all()
    return render(request, 'list.html', {'list_personne': personne})


def eleve_list(request):
    eleve = Etudiant.objects.all()
    return render(request,'eleve_list.html', {'eleve': eleve})


def eleve_create(request):
    #if not request.user.is_staff or not request.user.is_superuser:
     #   raise Http404

    if request.POST:
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/zak/eleve/all/')
    else:
        form = EtudiantForm()
    return render(request,'eleve_create.html', {'form': form})


def groupe_create(request):
    if request.POST:
        form = GroupeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/zak/groupe/all')
    else:
        form = GroupeForm()
    return render(request,'groupe_create.html', {'form': form})


def groupe_list(request):
    groupe = Groupe.objects.all()
    return render(request,'groupe_list.html', {'groupe': groupe})


def getClasseById(id_groupe):
    try:
        classe = Groupe.objects.get(pk=id_groupe)
    except Groupe.DoesNotExist:
        classe = None
    return classe


def eleve_groupe(request, id_groupe):
    groupe = getClasseById(id_groupe)
    eleve = Etudiant.objects.filter(groupe=groupe)
    return render(request,'eleve_groupe.html', {'liste_eleve': eleve})

def login(request):
    if request.post:
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/zak/accounts/loggedin')
    else:
        form = EtudiantForm()
    return render(request, 'login.html', {'form': form})


def loggedin(request):
    return render_to_response('loggedin.html',
                             {'full_name': request.user.username})

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')