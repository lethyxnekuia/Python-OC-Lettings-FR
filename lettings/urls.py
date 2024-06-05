from django.urls import path
from . import views
from .views import error_400_view, error_500_view

app_name = 'lettings'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]

handler400 = error_400_view
handler500 = error_500_view
