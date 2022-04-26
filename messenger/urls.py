from django.urls import path
from .views import BorrarMensaje, CrearMenssage, DetalleMensaje, MensajeList

urlpatterns = [path('',MensajeList.as_view(),name='message_list'),
path('crear_mensaje/',CrearMenssage.as_view(),name="message_create"),
path('detalle_mensaje/<pk>',DetalleMensaje.as_view(),name='message_detail'),
path("borrar_mensaje/<pk>/", BorrarMensaje.as_view(), name="message_delete"),
]
