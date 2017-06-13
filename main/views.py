from django.shortcuts import render


def connect(request):
    return render(request, 'html/connect.html', {})
# Create your views here.
