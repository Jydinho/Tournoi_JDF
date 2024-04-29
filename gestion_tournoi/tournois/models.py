from django.db import models

# Create your models here.
class Genre(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"nom : {self.nom}"


class ModeDeJeu(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"nom : {self.nom}"
    

class Jeu(models.Model):        
    nom = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    modes_de_jeux = models.ManyToManyField(ModeDeJeu)    

    def __str__(self):
        for el in self.genres:
            gn = gn + ' ' + str(el)
        for el in self.modes_de_jeux:
            mdj = mdj + ' ' + str(el)
        return f"nom : {self.nom}\n
                genres : {gn}\n
                modes de jeux : {mdj}\n"


class TypeDeTournoi(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"nom : {self.nom}"
    

class Adresse(models.Model):
    rue = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    commune = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=20)
    pays = models.CharField(max_length=80)

    def __str__(self):
        return f"rue            : {self.rue}\n 
        numero        : {self.numero}\n 
        commune       : {self.commune}\n 
        code_postal   : {self.code_postal}\n pays          : {self.pays}\n"


class Club(models.Model):
    nom = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=80)
    fk_adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)

    def __str__(self):
        return f"nom : {self.nom}, nationalite : {self.nationalite},
        adresse : {self.fk_adresse}"
    

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=254) #unique=True
    telephone = models.CharField(max_length=45, blank=True, null=True) 
    # blank=True va permettre de valider si le user ne rentre rien
    # null=True permet de créer la db ave une valeur null
    date_naissance = models.DateField(null=True, blank=True)
    nationalite = models.CharField(max_length=80)
    fk_adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    jeux = models.ManyToManyField(Jeu, on_delete=models.CASCADE)

    def __str__(self):
        print("La liste")
        return f"nom : {self.nom}\n
                prenom : {self.prenom}\n
                pseudo : {self.pseudo}, email : {self.email}\n
                telephone : {self.telephone}\n
                date de naissance {self.date_naissance}\n
                nationalite : {self.nationalite}\n
                adresse : {self.fk_adresse}\n
                jeux : {self.jeux}"



class Tournoi(models.Model):
    nom = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    nombre_de_place = models.IntegerField()
    paf = models.CharField(max_length=10, blank=True, null=True)
    reglement = models.TextField()
    fk_jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    fk_adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    




