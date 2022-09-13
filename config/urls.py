from django.contrib import admin
from django.urls import path, include

# Static
from django.conf import settings
from django.conf.urls.static import static

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quizes.urls')),
    path('', views.index, name='home'),
    path('ckeditor/',include('ckeditor_uploader.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)