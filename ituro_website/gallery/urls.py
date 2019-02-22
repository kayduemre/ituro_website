from django.conf.urls import url
from gallery.views import GalleryDetailView
from django.urls import path

urlpatterns = [

    path('<slug:slug>/', GalleryDetailView.as_view(),
        name="gallery_detail"),
]
