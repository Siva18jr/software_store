from django.shortcuts import render

def mobileApps(request):
    return render(request, 'android/home.html')

def mobileAppDetail(request):
    return render(request, 'android/app_detail.html')