
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views

## creating router object
router= routers.DefaultRouter()

# Register studentViewSet with router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
