from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Biodata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=20)
    telp = models.CharField(max_length=20) 
    alamat = models.TextField()

    def __str__(self):
        return "{}".format(self.nama) 