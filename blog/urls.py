from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.konten_list, name = 'konten_list'),   # Function Based View
    #path('', views.KontenListView.as_view(), name='konten_list'),    # Class Based View
    path('<int:year>/<int:month>/<int:day>/<slug:konten>/',
        views.konten_detail, name = 'konten_detail'),
    path('<int:konten_id>/share/',
        views.konten_share, name = 'konten_share'),
]
