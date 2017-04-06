from django.db import models


# Create your models here.
class Partia(models.Model):
    nazwa = models.CharField(max_length=40)


class Wybory(models.Model):
    typ = models.CharField(max_length=10)
    maxKandydatow = models.IntegerField
    czasWyboru = models.IntegerField


class Kandydat(models.Model):
    imie = models.CharField(max_length=15)
    nazwisko = models.CharField(max_length=20)
    licznik = models.IntegerField(default=0)
    partia = models.ForeignKey(Partia, on_delete=models.CASCADE)
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE)


class Glosujacy(models.Model):
    pesel = models.PositiveIntegerField()


class Glos(models.Model):
    glosujacy = models.ForeignKey(Glosujacy, on_delete=models.CASCADE)
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE)
