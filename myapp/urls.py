from django.contrib import admin
from django.urls import path
from app_name import views  # Replace 'app_name' with your app's name
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
]

# Add this for static file handling in development
if settings.DEBUG:  # Only serve static files this way during development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
