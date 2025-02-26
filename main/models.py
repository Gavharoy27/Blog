from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveSmallIntegerField(blank=True, null=True)
    kasb = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __get__(self):
        return self.ism


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=255)
    sana = models.DateTimeField(auto_now_add=True)
    matn = models.TextField(blank=True, null=True)
    mavzu = models.CharField(max_length=255)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha