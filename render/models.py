from django.db import models
from django import forms
# Create your models here.

class imagenApt(models.Model):
    Nombre = models.CharField(max_length=60)
    elevacion = models.DecimalField(max_digits=5,decimal_places=2)
    fecha =  models.DateField(auto_now_add=False)
    imagen = models.ImageField(upload_to="images/")
    audio = models.FileField(upload_to="audio/", null=True)

    class Meta :
        verbose_name = 'ImagenApt'
    def _str_(self):
       return self.Nombre

class imagenAptForm(forms.ModelForm):
    class Meta:
        model = imagenApt
        fields = ['Nombre', 'elevacion', 'fecha', 'imagen', 'audio']