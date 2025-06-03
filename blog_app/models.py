from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)

    def __str__(self):
        return self.nombre
    
class Posteo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) #Si el autor se elimina, los posteos asociados también se eliminan.

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre