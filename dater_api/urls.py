from django.urls import path

from . import views

app_name = 'dater_api'
urlpatterns = [
    path('view1', views.view1, name='view1'),
]

