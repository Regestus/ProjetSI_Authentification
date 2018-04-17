from django.db import models


# Create your models here.




class Personne(models.Model):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    numEtu = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nom


class Role(models.Model):
    nom = models.CharField(max_length=30)
    valeur = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom


class Groupe(models.Model):
    nom = models.CharField(max_length=30)
    annee = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Domaine(models.Model):
    nom=models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom


class Etudiant(Personne):
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.groupe


class Enseignant(Personne):
    specialite = models.ForeignKey(Domaine, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.specialite


