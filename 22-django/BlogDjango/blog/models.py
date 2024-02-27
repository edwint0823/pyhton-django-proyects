from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null', null=True, verbose_name="Imagen", upload_to='articles')
    public = models.BooleanField(default=False, verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    user = models.ForeignKey(User, verbose_name="Usuario", editable=False, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", blank=True)

    # categories = models.ManyToManyField(Category, verbose_name="Categorías", blank=True, related_name="articles" )

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
