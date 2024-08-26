from django.shortcuts import render


def error_404_view(request, exception):
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    return render(request, 'error_404.html', status=404)


def error_500_view(request):
    return render(request, 'error_500.html', status=500)
