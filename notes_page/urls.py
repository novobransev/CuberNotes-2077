from django.urls import path
from .views import *


urlpatterns = [
    path('note/create/', BlogCreateView.as_view(), name='post_new'),  # Здесь создается заметка
    path('note/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # Здесь мы можем просмотреть содержимое
    path('note/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), # Здесь можно обновить заметку
    path('note/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'), # Здесь можно удалить заметку
    path('note/<int:pk>/complete/', CompleteView.as_view(), name='post_complete'), # Здесь можно удалить заметку
    path('', BlogListView.as_view(), name='home'),
    path('home_complete/', ListCompleteView.as_view(), name='home_complete'),
]
