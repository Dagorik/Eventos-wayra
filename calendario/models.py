from django.db import models

class Evento(models.Model):
  	starup = models.CharField(max_length = 50, null = False, default = '')
  	fecha = models.DateField()
  	hora = models.TimeField(auto_now=False, auto_now_add=False)
  	titulo = models.CharField(max_length = 25, null = False, default = '')
  	descripcion = models.TextField(max_length = 140, null = False, default = '')
  	imagenes = models.ImageField(upload_to='media/')
  	video = models.URLField(max_length=200)
  	invitadoMail = models.EmailField(max_length=50)
  

    def __str__(self):
        return self.titulo

