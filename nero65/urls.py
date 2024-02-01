from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TracksListView.as_view(), name='tracks_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('tracks_list_favorite/', FavoriteTracksListView.as_view(), name='tracks_list_favorite'),
    path('tracks_top/', TopLikedTracksListView.as_view(), name='tracks_top'),
    path('like_create/<int:track_id>/', CreateLikeView.as_view(), name='like_create'),
    path('like/<int:track_id>/delete/', DeleteLikeView.as_view(), name='like_delete'),
    path('track_create/', TrackCreateView.as_view(), name='track_create'),
    path('track_update/<int:pk>/', TrackUpdateView.as_view(), name='track_update'),
    path('track_about/<int:pk>/', TrackDetailView.as_view(), name='track_about'),
    path('track_delete/<int:pk>/', TrackDeleteView.as_view(), name='track_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

