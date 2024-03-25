from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('word_list', views.word_list, name='list'),
    path('word_list/', views.word_list, name='list'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)