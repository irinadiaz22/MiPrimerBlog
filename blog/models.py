from django.db import models
from django.utils import timezone
#creacion de modelos, definir clases usando.. Class Nombre con sus atributos
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) #tipocaracter con limite
    text = models.TextField() # texto sin limites
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True) # blank->permite blancos  null->permite nulos
            #METODOS
    def publish(self): #METODO publicar
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #METODO PONER TITULO
        return self.title
