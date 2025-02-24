from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'groups', views.GroupViewSet, basename='groups')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),

    re_path(
        r'^posts/(?P<post_id>\d+)/comments/$',
        views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post-comments-list'
    ),
    re_path(
        r'^posts/(?P<post_id>\d+)/comments/(?P<pk>\d+)/$',
        views.CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='post-comment-detail'
    ),
]
