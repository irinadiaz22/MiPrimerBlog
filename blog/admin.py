from django.contrib import admin #importar Libreria admin de Django
from .models import Post #importa modelo Post que yo cree

admin.site.register(Post) 
