from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import bcrypt


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user and bcrypt.checkpw(password.encode(), user.password.encode()):
        # autenticação bem-sucedida, gere um token JWT para o usuário
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return Response({'token': token}, status=status.HTTP_200_OK)
    else:
        # falha na autenticação
        return Response({'detail': 'Usuário e/ou senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)
