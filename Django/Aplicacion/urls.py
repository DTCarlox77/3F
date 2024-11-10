from django.urls import path
from .views import * # Importamos la vista main de la aplicacion

urlpatterns = [ # SIEMPRE se debe agregar un / al final de la URL
    path('', index, name='index'), # Agregamos la URL de la vista index
    path('prueba/', main, name='main'),
    path('frutas/', frutas, name='frutas'),
    path('fantasma/', fantasma, name='fantasma'),
    path('saludar/<str:nombre>', saludar),
    path('formulario/', formulario, name='formulario'),
    path('fruta/<int:id>/', especifica, name='especifica'),
    path('eliminar/<int:id>/', eliminar, name='eliminar')
    # <int:variable>, <str:variable>, <float:variable>
]
