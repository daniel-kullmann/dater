"""dater URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dater_api.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name="home_empty"),
    path('index.html', TemplateView.as_view(template_name='index.html'), name="home"),
]
