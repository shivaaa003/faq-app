from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet


router = DefaultRouter()
router.register(r'faq', FAQViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),  # The admin panel
    path('api/', include(router.urls)),  # The API URLs
    path('', views.home),  # Root URL 
]
