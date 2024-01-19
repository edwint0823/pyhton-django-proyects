from pages.models import Page


def get_pages(request):
    pages = Page.objects.values_list('id', 'title', 'slug')
    print(pages)
    return {'pages': pages}
