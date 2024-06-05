from django.shortcuts import render
from .models import Letting


def home(request):
    return render(request, 'lettings/home.html')


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)


def error_400_view(request, exception):
    return render(request, 'error_400.html', status=400)


def error_500_view(request):
    return render(request, 'error_500.html', status=500)
