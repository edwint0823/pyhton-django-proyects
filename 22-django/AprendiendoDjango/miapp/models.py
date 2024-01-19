from django.db import models

# Create your models here.
"""
Crear migración a partir de modelos
# tener la app registrada en settings.py
# en la carpeta del proyecto correr python manage.py makemigrations (crear un archivo en migrations)
# para visualizar código sql de la migración
    # en la carpeta del proyecto correr python manage.py sqlmigrate <nombre_app> <numero_de_migracion>
        # ej: python manage.py sqlmigrate miapp 0001
# para reflejar los cambios de la migración en db 
    # en la carpeta del proyecto correr python manage.py migrate
#para realizar un cambio sobre las tablas (modifiar , crear o eliminar un campo)
    #se realiza el cambio en este archivo
    # se ejecuta el comando python manage.py makemigrations
"""


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default="null", verbose_name="Imagen", upload_to='articles')
    public = models.BooleanField(verbose_name="¿Publico?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        # db_table
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        # orden en los elementos se muestran en el panel de administración
        ordering = ['id']

    def __str__(self):
        if self.public:
            publico = "(Publicado)"
        else:
            publico = "(Privado)"
        return f"{self.title} {self.image} {publico}"


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        # db_table
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
