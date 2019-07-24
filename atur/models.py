from django.db import models

# Create your models here.
class Blog(models.Model):
    nama_file = models.CharField(max_length=255)
    tanggal = models.DateField(auto_now=True)
    tanggalinput = models.DateField()
    jam = models.TimeField(auto_now=True)
    jaminput = models.TimeField()
    integ = models.IntegerField()
    isi = models.TextField()
    tempat = models.URLField()
