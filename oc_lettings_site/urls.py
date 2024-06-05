from django.contrib import admin
from django.urls import path, include
from lettings.views import home


urlpatterns = [
    path('', home, name='home'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
