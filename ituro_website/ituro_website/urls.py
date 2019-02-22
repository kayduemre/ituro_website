from django.urls import include, path
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from gallery.sitemaps import GallerySitemap
from post.sitemaps import AboutEntrySitemap,CategoryEntrySitemap,CommonEntrySitemap, \
    NewsEntrySitemap,SponsorshipEntrySitemap


sitemaps = {
    'news' : NewsEntrySitemap,
    'about' : AboutEntrySitemap,
    'category' : CategoryEntrySitemap,
    'sponsorship' : SponsorshipEntrySitemap,
    'gallery' : GallerySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path(r'robots\.txt', include('robots.urls')),
]

urlpatterns += i18n_patterns(

    path('i18n/', include('django.conf.urls.i18n')),
    path(r'sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path(_(r'^gallery/'), include(("gallery.urls", "gallery"),namespace="gallery")),
    path(' ', include(("post.urls", "survey"), namespace="post")),
    path(_('survey/'), include(("survey.urls", "survey"), namespace="survey")),

)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
