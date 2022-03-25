from django.urls import path
from . import views

urlpatterns = [
    path('api/resources', views.ResourceList.as_view(), name='resource_list'),
    path('api/resources/<int:pk>', views.ResourceDetail.as_view(), name='resource_detail'),
    path('api/forum', views.ForumList.as_view(), name='forum_list'),
    path('api/forum/<int:pk>', views.ForumDetail.as_view(), name='forum_detail'),
]
