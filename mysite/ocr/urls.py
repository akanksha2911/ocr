from django.contrib import admin
from django.urls import path
from ocr import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path("",views.index,name='ocr'),
    path('choice', views.choice, name='choice'),
    path('convertor', views.convertor, name='convertor'),
    path('setTimer',views.setTimer,name='setTimer'),
    path('scd',views.scd,name='scd')
] 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)