from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        data = {
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "phone": user.phone,
            "location": user.location,
        }

        return Response(data)