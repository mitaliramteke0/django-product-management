from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, RegisterView, LoginView, LogoutView, BulkUploadView



router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="category")
router.register(r'products', ProductViewSet, basename="product")


urlpatterns = [
    path('', include(router.urls)),
      
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('upload/', BulkUploadView.as_view()),  # Bulk upload endpoint

]