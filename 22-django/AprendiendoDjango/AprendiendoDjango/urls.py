"""
URL configuration for AprendiendoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from miapp import views as mi_app

# PARA CREAR UN USUARIO ADMINISTRADOR
"""
 comando python manage.py createsuperuser 
 genera un asistente donde consulta las credenciales
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mi_app.index, name='index'),
    path('inicio/', mi_app.index, name='inicio'),
    path('pagina/', mi_app.pagina, name='pagina'),
    path('pagina/<int:redirigir>', mi_app.pagina, name='pagina'),
    path('hola-mundo/', mi_app.hola_mundo, name='hola_mundo'),
    path('contacto/', mi_app.contacto, name='contacto'),
    path('contacto/<str:nombre>/', mi_app.contacto, name='contacto'),
    path('contacto/<str:nombre>/<str:apellidos>', mi_app.contacto, name='contacto'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', mi_app.crear_articulo, name='crear_articulo'),
    path('articulo/', mi_app.get_articulo, name='articulo'),
    path('editar-articulo/<int:id>', mi_app.editar_articulo, name='editar_articulo'),
    path('listar-articulos', mi_app.listar_articulos, name='listar_articulos'),
    path('delete-articulo/<int:id>', mi_app.borrar_articulo, name='borrar_articulo'),
    path('save-article/', mi_app.save_article, name='save'),
    path('create-article/', mi_app.create_article, name='create'),
    path('create-full-article/', mi_app.create_full_article, name='create_full'),
    path('register-order/', mi_app.register_order, name='velas')
]

# coinfiguracion para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
