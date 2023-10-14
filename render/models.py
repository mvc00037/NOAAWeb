from django.db import models

# Create your models here.

class imagenApt(models.Model):
    Nombre = models.CharField(max_length=60)
    elevacion = models.DecimalField(max_digits=5,decimal_places=2)
    fecha =  models.DateField(auto_now_add=False)
    imagen = models.ImageField(upload_to = "media/noaaWebApp")
    audio = models.FileField(upload_to = "media/noaaWebApp", null=True)

    class Meta :
        verbose_name = 'ImagenApt'
    def _str_(self):
       return self.Nombre