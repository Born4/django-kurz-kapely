from django.urls import path, include

from bands.views import (band_list_view, band_detail_view,
                         band_manual_form_create_view, band_create_view,
                         band_update_view, band_delete_view, BandListViewGeneric, BandDetailViewGeneric,
                         BandCreateViewGeneric, BandUpdateViewGeneric, BandDeleteViewGeneric,
                         TestGetParametru, AlbumListView, BandUpdateView)

app_name = 'bands'
urlpatterns = [
    # path('band-listing/', band_list_view, name='band-listing'),
    path('band-listing/', BandListViewGeneric.as_view(), name='band-listing'),
    # path('band-listing/', BandListView.as_view(), name='band-lising'),

    # path('band-detail/<int:pk>/', band_detail_view, name='band-detail'),
    path('band-detail/<int:pk>/', BandDetailViewGeneric.as_view(), name='band-detail'),
    # path('band-detail/<int:pk>/', BandDetailView.as_view(), name='band-detail'),

    path('manual-form/', band_manual_form_create_view, name='manual-form'),
    # path('band-create/', band_create_view, name='band-create'),
    path('band-create/', BandCreateViewGeneric.as_view(), name='band-create'),
    # path('band-create/', BandCreateView.as_view(), name='band-create'),

    # path('band-update/<int:pk>/', band_update_view, name='band-update'),
    # path('band-update/<int:pk>/', BandUpdateViewGeneric.as_view(), name='band-update'),
    path('band-update/<int:pk>/', BandUpdateView.as_view(), name='band-update'),

    # path('band-delete/<int:pk>/', band_delete_view, name='band-delete'),
    path('band-delete/<int:pk>/', BandDeleteViewGeneric.as_view(), name='band-delete'),
    # path('band-delete/<int:pk>/', BandDeleteView.as_view(), name='band-delete'),

    path('get-parametry/', TestGetParametru.as_view(), name='tes-get-params'),

    path('album-listing/', AlbumListView.as_view(), name='album-listing'),

]
