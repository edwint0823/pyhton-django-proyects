from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from miapp.models import Article
from miapp.forms import FormArticle
from django.contrib import messages


# Create your views here.
# MVC = Modelo Vista Controlador → acciones (metodos)
# MVC = Modelo Template Vista → acciones (metodos)


def index(request):
    year = 2023
    years = range(year, 2051)
    """
    while year <= 2050:
        years.append(year)
        year += 1
    """

    lenguajes = ['PHP', 'Python', 'Java', 'JavaScript', 'TypeScript']
    return render(request, 'index.html', {'year': year, 'years': years, 'lenguajes': lenguajes, 'nombre': 'Edwin'})


def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect("contacto", nombre="Edwin", apellidos="Ariza")
    return render(request, 'pagina.html', {'texto': '', 'lista': ['una', 'dos', 'tres', 'cuatro']})


def contacto(request, nombre="", apellidos=""):
    return render(request, 'contacto.html', {'nombre': nombre, 'apellidos': apellidos})


# def contacto(request, nombre="", apellidos=""):
#     return HttpResponse(layout + f"<h2>Contacto {nombre} {apellidos}</h2>")

def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} - {articulo.public}")


def save_article(request):
    # if request.method == "GET":
    # title = request.GET.get("title")
    # title = request.GET["title"]
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        public = request.POST.get("public")
        articulo = Article(
            title=title,
            content=content,
            public=public
        )
        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} - {articulo.public}")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")


def create_article(request):
    return render(request, 'create_articulo.html')


def create_full_article(request):
    if request.method == "POST":
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get("title")
            content = data_form.get("content")
            public = data_form["public"]
            articulo = Article(
                title=title,
                content=content,
                public=public
            )
            articulo.save()
            # return HttpResponse(f"{articulo.title} - {articulo.content} - {str(articulo.public)}")
            # mensaje flash
            messages.success(request, f"Se guardo el articulo socio {articulo.id}")
            return redirect("listar_articulos")
    else:
        formulario = FormArticle()
    return render(request, 'create_full_articulo.html', {'formulario': formulario})


def get_articulo(request):
    try:
        articulo = Article.objects.get(id=2)
        # articulo = Article.objects.get(id=2, public=True)
        # articulo = Article.objects.get(pk=2)
        response = f"Articulo {articulo.id} {articulo.title} - {articulo.content} - {articulo.public}"
    except:
        response = 'No existe el articulo'
    return HttpResponse(response)


def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Teclado"
    articulo.content = "Teclado logitech"
    articulo.public = True
    articulo.save()
    return HttpResponse(f"Articulo editado: {articulo.title} - {articulo.content} - {articulo.public}")


def listar_articulos(request):
    articulos = Article.objects.all()
    # sin "-" Asc con "-" Desc
    # articulos = Article.objects.order_by('-id')
    # limit [offset:limit] si no se requiere offset [:limit] sirve con all()
    # articulos = Article.objects.order_by('-id')[2:1]

    # articulos = Article.objects.filter(public=True, title="Teclado")
    # LOOCKUPS
    # like
    # articulos = Article.objects.filter(title__contains="Tec")
    # exac
    # articulos = Article.objects.filter(title__exact="Tec")
    # gt - gte lt-lte
    # articulos = Article.objects.filter(id__gte=3)
    # exclude
    # articulos = Article.objects.filter(title="Teclado").exclude(public=False)
    # Raw
    # articulos = Article.objects.raw('SELECT * FROM miapp_article WHERE public=1')
    # OR
    # articulos = Article.objects.filter(
    #     Q(title__contains="te") | Q(title__contains="co")
    # )
    return render(request, 'articulos.html', {"articulos": articulos})


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')


def register_order(request):
    candle_type_list = [
        {
            'id': 0,
            'name': 'Vela blanca letra negra cursiva',
            'img': 'images/logo.png',
        },
        {
            'id': 1,
            'name': 'Deseos vela blanca letra negra cursiva',
            'img': 'images/logo.png',
        },
        {
            'id': 2,
            'name': 'Pesebre x6',
            'img': 'images/logo.png',
        },
        {
            'id': 3,
            'name': 'Vela de colores letra negra ST',
            'img': 'images/logo.png',
        },

    ]
    return render(request, 'velas_v1.html', {'candle_type_list': candle_type_list})
