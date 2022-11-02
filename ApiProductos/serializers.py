from dataclasses import fields
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model= Producto
    fields=('id','nombre','precio','descripcion','stock','marca','modelo','fechaVenta','horaVenta','iva','imagen')
    read_only_fields=('fechaVenta','horaVenta',)