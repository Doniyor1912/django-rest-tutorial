from typing import _generic_init_subclass

from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from api.models import Container
from api.serializers import SerializerPerson

@extend_schema_view(
    list=extend_schema(summary='List Category', tags=['Container']),
    retrieve=extend_schema(summary='Retrieve Category', tags=['Container']),
    create=extend_schema(summary='Create Category', tags=['Container']),
    update=extend_schema(summary='Update Category', tags=['Container']),
    partial_update=extend_schema(summary='Partial_update Category', tags=['Container']),
    destroy=extend_schema(summary='Destroy Category', tags=['Container'])
)
#viewsets-->mixins------------------
class Person(mixins.CreateModelMixin,
             mixins.ListModelMixin,
             mixins.RetrieveModelMixin,
             mixins.UpdateModelMixin,
             mixins.DestroyModelMixin,
                GenericViewSet):
    queryset = Container.objects.all()
    serializer_class = SerializerPerson

#----------------------------


#get-all --> malumotlar kelishini cheklash uchun------
    def get_queryset(self, pk=None,*args, **kwargs):
        pk = self.kwargs.get("pk")
        if not pk:
            return Container.objects.all()[:3]
        return Container.objects.filter(pk=pk)

#-----------------------------------
