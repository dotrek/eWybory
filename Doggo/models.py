from django.db import models

# Create your models here.
class Partia(models.Model):
    nazwa = models.CharField(max_length=40)

    __tablename__ = 'Partia'

    def __str__(self):
        return self.nazwa


class Wybory(models.Model):
    id = models.AutoField(primary_key=True)
    typ = models.CharField(max_length=10)
    start_time = models.DateField()
    end_time = models.DateField()
    maxKandydatow = models.IntegerField(default=0)
    # czasWyboru = models.IntegerField(default=0)

    __tablename__ = 'Wybory'

    def __str__(self):
        return "%s" % (self.typ)


class Kandydat(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=15)
    nazwisko = models.CharField(max_length=20)
    licznik = models.IntegerField(default=0)
    partia = models.ForeignKey(Partia, on_delete=models.CASCADE)
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s - %s" % (self.imie, self.nazwisko, self.partia)


class Glosujacy(models.Model):
    id = models.AutoField(primary_key=True)
    pesel = models.BigIntegerField(unique=True)

    def __str__(self):
        return "%d" %self.pesel


class Glos(models.Model):
    id = models.AutoField(primary_key=True)
    glosujacy = models.ForeignKey(Glosujacy, on_delete=models.CASCADE)
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE)


class Kandydowanie(models.Model):
    kandydat = models.ForeignKey(Kandydat, on_delete=models.CASCADE)
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE)
    __tablename__ = 'Kandydowanie'

    def __str__(self):
        return "%s %s w wyborach %s" % (self.kandydat.imie, self.kandydat.nazwisko, self.wybory.typ)
