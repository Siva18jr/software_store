from django.shortcuts import render

def mobileAppDetail(request):
    return render(request, 'mobile-apps/app_detail.html')