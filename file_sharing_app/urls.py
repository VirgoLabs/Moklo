from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('track/<uuid:file_id>/', views.track_file, name='track_file'),
    path('download/<uuid:file_id>/', views.download_page, name='download_page'),
    path('download/<uuid:file_id>/go/', views.execute_download, name='execute_download'),
]