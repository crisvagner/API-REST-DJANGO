from rest_framework import serializers
from Notes.models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'content']

    def create(self, validated_data):
        # Obtém o ID do usuário autenticado a partir do contexto da requisição
        user_id = self.context['request'].user.id

        # Cria uma nova nota, vinculando-a ao usuário autenticado
        note = Notes.objects.create(author_id=user_id, **validated_data)

        return note
