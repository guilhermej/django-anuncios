from django.urls import path

from .views import home
from .views import categoria

urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:categoria_id>', categoria, name='categoria'),
]


