from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from Notes.api.serializers import NotesSerializer
from Notes.models import Notes


# ViewSet para as Notas
class NotesViewSet(viewsets.ModelViewSet):
    # Define a classe do serializer que será usada para serializar e desserializar as Notas
    serializer_class = NotesSerializer
    # Define o queryset a ser usado para recuperar as Notas a partir do banco de dados
    queryset = Notes.objects.all()

    # Define que a autenticação das requisições será feita com JWT
    authentication_classes = [JWTAuthentication]
    # Define que apenas usuários autenticados poderão acessar esta ViewSet
    permission_classes = [IsAuthenticated]

    # Sobrescreve o método get_queryset para retornar apenas as Notas do usuário autenticado
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        if user is not None:
            queryset = queryset.filter(author_id=user.id)
        return queryset
