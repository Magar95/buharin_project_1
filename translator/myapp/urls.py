from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('home/', views.index, name='index'),

    path('words_list', views.words_list, name='word_list'),
    path('words_list/', views.words_list, name='word_list'),

    path('add_word', views.add_word, name='add_word'),
    path('add_word/', views.add_word, name='add_word'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)