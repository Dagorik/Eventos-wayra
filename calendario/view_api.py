from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, status, generics, viewsets
from django.shortcuts import get_object_or_404
from .serializer import EventoSerializer
from .models import Evento

class EventoListado(generics.ListCreateAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('fecha', 'titulo', 'starup')

class EventoDetalleView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

