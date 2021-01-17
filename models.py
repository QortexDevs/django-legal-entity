from django.db import models


class CEO(models.Model):
    name = models.CharField(max_length=200)
    inn = models.CharField(max_length=20, unique=True,
                           db_index=True, default=None)

    def __str__(self):
        return self.name


class LegalEntity(models.Model):
    name = models.CharField(max_length=300)
    inn = models.CharField(max_length=20, unique=True, db_index=True)
    ogrn = models.CharField(max_length=20)
    kpp = models.CharField(max_length=20)
    ceo = models.ForeignKey(CEO, on_delete=models.PROTECT, db_index=True)

    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=300)
    inn = models.CharField(max_length=20, unique=True, db_index=True)
    kpp = models.CharField(max_length=20)
    bik = models.CharField(max_length=20, unique=True, db_index=True)
    correspondent_account = models.CharField(max_length=40)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
