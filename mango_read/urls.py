

from django.contrib import admin
from django.urls import path, include
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('api/v1/genres/', views.GenreAPIView.as_view()),
    path('api/v1/genres/<int:pk>', views.GenreRetrieveUpdateDelete.as_view()),
    path('api/v1/cards/',views.CardModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/cards/<int:pk>', views.CardModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/comments/', views.CommentModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/comments/<int:pk>', views.CommentModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
