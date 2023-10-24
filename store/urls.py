from django.urls import path
from . import views

urlpatterns = [
    path('detail', views.mobileAppDetail, name="mobileAppsDetail")
]