from django.urls import path
from . import views

urlpatterns = [
    path('android/', views.mobileApps, name="androidApps"),
    path('android/detail', views.mobileAppDetail, name="androidAppsDetail")
]