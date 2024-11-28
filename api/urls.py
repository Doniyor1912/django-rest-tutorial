
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.spectacular.urls import urlpatterns as doc_urls
from api.views import Person

app_name = 'api'

# router = SimpleRouter()
# router.register('', Person, basename='path')

urlpatterns = [
    path('Person/create-category/',Person.as_view({'post': 'create'})),
    path('Person/getlist-category/', Person.as_view({'get': 'list'})),
    path('Person/put-category/<int:pk>/', Person.as_view({'put': 'update'})),
    path('Person/patch-category/<int:pk>/', Person.as_view({'patch': 'partial_update'})),
    path('Person/delete-category/<int:pk>/', Person.as_view({'delete': 'destroy'})),
    path('Person/get-category/<int:pk>/', Person.as_view({'get': 'retrieve'})),

]


urlpatterns += doc_urls