from typing import _generic_init_subclass

from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins, generics
from rest_framework.viewsets import GenericViewSet
from rest_framework import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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

#generics-----------------------
class Unity(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = SerializerPerson
    permission_classes = (IsAuthenticatedOrReadOnly,)

#-------------------------

#get-all --> malumotlar kelishini cheklash uchun------
    def get_queryset(self, pk=None,*args, **kwargs):
        pk = self.kwargs.get("pk")
        if not pk:
            return Container.objects.all()[:3]
        return Container.objects.filter(pk=pk)

#-----------------------------------



#action-------
    @action(methods=['get'],detail=True)
    def category(self,request, pk=None):
        pk = self.kwargs.get("pk")
        if not pk:
            return Person.objects.all()
        return Person.objects.filter(pk=pk)
#-----------------


class PersonList(APIView):

    def get(self,request, *args, **kwargs):
        pk = self.kwargs.get("pk",None)
        if pk:
            if not pk:
                return Response({"Answer":"Get not allowed"})
            try:
                instance = Person.objects.get(pk=pk)

            except:
                return Response({"Answer": "Data not found"})

            serializer = SerializerPerson(instance)
            return Response({"Person":serializer.data})

        else:
            list_person = Person.objects.all()
            return Response({"Person":SerializerPerson(list_person, many=True).data})

    def post(self,request):
        serializer = SerializerPerson(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Person":serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Answer": "Method Put not allowed!"})
        try:
            intance = Person.objects.get(pk=pk)

        except:
            return Response({"Answer": "DAta not found!"})

        serializer = SerializerPerson(data=request.data, instance=intance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Person":serializer.data})


    def pacht(self, request, *args, **kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response({"Answer": "Method pacht not allowed!"})
        try:
            instance = Person.objects.get(pk=pk)

        except:
            return Response({"Answer": " Data not found!"})

        serializer = SerializerPerson(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Person": serializer.data})



    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Answer": "Method Delete not allowed!"})

        try:
            instance = Person.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"Answer": "Data not found!"})

        return Response({"Person":f"{pk}-id -> deleted"})








