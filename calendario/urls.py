from django.conf.urls import url, include
from .view_api import EventoListado, EventoDetalleView

urlpatterns =[
  url(r'^$', EventoListado.as_view()),
  url(r'^(?P<pk>[0-9]+)/$', EventoDetalleView.as_view()),
]