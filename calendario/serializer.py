from rest_framework import serializers
from .models import Evento

class EventoSerializer(serializers.ModelSerializer):
	class Meta:
		models = Evento
		fields = '__all__'
