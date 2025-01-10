from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth import logout, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer



class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try: 
            username = request.data.get('username')
            password = request.data.get('password')
            email = request.data.get('email')
            imageURL = request.data.get('imageURL')
            print(f"Request data: {request.data}")

            if not username or not password:
                return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                imageURL=imageURL
            )
            user.save()

                
            serializer = UserSerializer(user)
            return Response({'message': 'User created successfully -backend', 'user': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error creating user: {e}")
            return Response({'error': 'Failed to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        print("Request data:", request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        print(f"Username: {username}, Password: {password}")
        
        print(request.data)
        
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=username, password=password)
        print("Authenticated user:", user)
        if user:
            # Generate the token for the user
            token, created = Token.objects.get_or_create(user=user)
            print(f"TOKEN: {token}")
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request)
        request.auth.delete()  # Destroy the token
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class VerifyTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
