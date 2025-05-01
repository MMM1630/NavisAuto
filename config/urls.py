from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from config import settings
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to NavisAuto!") 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auto.urls')),
    path('', home),  # Главная страница
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)