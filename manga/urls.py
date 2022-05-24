
from django.urls import path

from . import views

app_name = 'manga'
urlpatterns = [
    path('', views.ChapterListView.as_view(), name='home'),
    path('<int:pk>/', views.PostPageView.as_view(), name='postpage'),
]
