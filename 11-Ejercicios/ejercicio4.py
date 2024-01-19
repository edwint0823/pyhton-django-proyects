def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = 'lista'
    elif tipo == str:
        result = 'string'
    elif tipo == int:
        result = 'integer'
    elif tipo == bool:
        result = 'boolean'

    return result


def verificaTipo(variable, tipo):
    test = isinstance(variable, tipo)
    if test:
        return f"Este dato es de tipo {traducirTipo(tipo)}"
    else:
        return f"Este dato no es de tipo {traducirTipo(tipo)}"


mi_lista = ["texto", "texto", "texto", "texto"]
mi_string = "texto de prueba"
mi_numero = 1200
mi_bolean = True

print(verificaTipo(mi_lista, str))
print(verificaTipo(mi_string, str))
print(verificaTipo(mi_numero, int))
print(verificaTipo(mi_bolean, bool))
