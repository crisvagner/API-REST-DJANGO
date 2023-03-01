from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, generics

from django.contrib.auth.models import User
from Users.api.serializers import UsersSerializer


# Cria uma view para criar usuários
class CreateUserView(generics.CreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]


# Cria uma view para visualizar, atualizar e deletar usuários
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()

    # Define a autenticação utilizada como JWT
    authentication_classes = [JWTAuthentication]

    # Define as permissões necessárias para acessar a view
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user

        # Filtra o queryset para exibir apenas o usuário autenticado
        if user is not None:
            queryset = queryset.filter(id=user.id)
        return queryset
