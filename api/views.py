from rest_framework import viewsets, status
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, UserSerializer,LoginSerializer
from .tasks import bulk_upload
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.contrib.auth import get_user_model
User = get_user_model()

# ===== Authentication Views ===== #

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    serializer_class = LoginSerializer  # ✅ Add this to fix assertion error

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(email=email, password=password)

        if user:
            return Response({"message": "Login successful"})
        return Response({"error": "Invalid credentials"}, status=400)

class LogoutView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.auth.delete()
        return Response({"message": "Logout successful"})

class UpdateUserView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class BulkUploadView(APIView):
    def post(self, request):
        bulk_upload.delay(request.data)
        return JsonResponse({"message": "Bulk upload started!"})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

# ===== Product Management ===== #
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
