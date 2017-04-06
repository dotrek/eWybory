from django.db import models


# Create your models here.
class Partia(models.Model):
    nazwa = models.CharField(max_length=40)

    __tablename__ = 'Partia'

    def __str__(self):
        return self.nazwa


class Wybory(models.Model):
    typ = models.CharField(max_length=10)
    maxKandydatow = models.IntegerField
    czasWyboru = models.IntegerField

    def __str__(self):
        return "%s %d %d" % (self.typ, self.maxKandydatow, self.czasWyboru)


class Kandydat(models.Model):
    imie = models.CharField(max_length=15)
    nazwisko = models.CharField(max_length=20)
    licznik = models.IntegerField(default=0)
    partia = models.ForeignKey(Partia, on_delete=models.CASCADE)
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %d" % (self.imie, self.nazwisko, self.licznik)


class Glosujacy(models.Model):
    pesel = models.PositiveIntegerField()

    def __str__(self):
        return self.pesel


class Glos(models.Model):
    glosujacy = models.ForeignKey(Glosujacy, on_delete=models.CASCADE)
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE)
