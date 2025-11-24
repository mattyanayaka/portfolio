from django.urls import path
from . import views
from .views import FriendList
from .views import FriendDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('list', FriendList.as_view()), #☆
    path('detail/<int:pk>', FriendDetail.as_view()), #☆
    path('find', views.find, name='find'), #☆,
    path('<int:num>', views.index, name='index'),
]