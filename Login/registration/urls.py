from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout_view'),
    path('protegida/',protegida, name='protegida')
]
