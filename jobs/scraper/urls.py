from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newview', views.new_view, name="new_view")
]