from django.urls import path
from . import views

app_name = 'netops'
urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.service_add, name='service_add'),
    path('services/<int:id>', views.service_update, name='service_update')
]