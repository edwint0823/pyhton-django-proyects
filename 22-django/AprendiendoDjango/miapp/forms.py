from django import forms
from django.core import validators


class FormArticle(forms.Form):
    general_attrs = {
        "placeholder": "Titulo",
        'class': 'titulo_form_article'
    }
    title = forms.CharField(
        label="Titulo",
        max_length=50,
        widget=forms.TextInput(
            attrs=general_attrs
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(20, 'El contenido es demasiado largo')
        ]
    )
    # content.widget.attrs.update(general_attrs)
    content.widget.attrs.update({
        "placeholder": "Contenido del articulo",
        'class': 'content_form_article'
    })
    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label="Publicado",
        choices=public_options
    )
