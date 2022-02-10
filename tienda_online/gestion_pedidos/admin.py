from django.contrib import admin
from gestion_pedidos.models import Articulos, Clientes, Pedidos

# registro modelos

admin.site.register(Articulos)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Pedidos)
