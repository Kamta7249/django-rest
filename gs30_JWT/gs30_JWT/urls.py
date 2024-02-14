"""
URL configuration for gs17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


# Create Router Object
router = DefaultRouter()

# Register StudentModelViewSet with Router
router.register('studentapi',views.StudentModelViewSet, basename='student')

# # Register SStudentReadOnlyModelViewSet with Router
# router.register('studentapi',views.StudentReadOnlyModelViewSet, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refeshtoken/',TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(), name='token_verify'),


    
]
