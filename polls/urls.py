from django.urls import path
from . import views

app_name='polls'

urlpatterns = [
    path('', views.home, name='home'),
    path('polls/', views.index, name='index'),
    path('polls/<int:q_id>/',views.detail,name='detail'),
    path('polls/<int:q_id>/vote/',views.vote,name='vote'),
    path('polls/<int:q_id>/result/',views.result,name='result'),
]