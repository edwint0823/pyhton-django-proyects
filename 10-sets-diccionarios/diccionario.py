personas = {
    'nombre': 'Juan',
    'apellidos': 'Pepe',
    "web": "vicotorobleswe.es"
}

print(personas)
print(type(personas))

print(personas['nombre'])

contactos = [
    {
        'nombre': 'Juan',
        "email": "juan@juan.com"
    },
    {
        'nombre': 'Luis',
        "email": "luis@luis.com"
    }
]

print(contactos[0]['nombre'])

for contacto in contactos:
    print(f"Nombre {contacto['nombre']} email {contacto['email']}")
