from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import (
    PostListView,
    PostDetailView,
)
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('',PostListView.as_view(),name='home'),
    path("<slug>/",PostDetailView.as_view(), name='detail')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
