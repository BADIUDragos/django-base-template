from django.urls import path
from DjangoProject import views

app_name = 'Application'
urlpatterns = [
    path('', views.project_index, name='index'),
]