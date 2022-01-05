from django.db import models
import datetime

class Kategori(models.Model):
    nama = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "1. Kategori"

class Artikel(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    judul = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

    class Meta:
        ordering =['-id']
        verbose_name_plural = "2.Artikel"
