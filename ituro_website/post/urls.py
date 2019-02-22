from django.conf.urls import url
from django.urls import path
from django.utils.translation import ugettext_lazy as _
from post.views import HomePageDetailView, AboutDetailView, \
    CategoryDetailView, SponsorshipDetailView, CommonDetailView, \
    NewsEntryDetailView, contactView, successView


urlpatterns = [

    path('', HomePageDetailView.as_view(), name="homepage"),
    path(_('contact_us/'), contactView, name="contact"),
    path(_('success/'), successView, name="success"),
    path(_('about/<slug:slug>/'), AboutDetailView.as_view(),
        name="about_detail"),
    path(_('category/(<slug:slug>/'), CategoryDetailView.as_view(),
        name="category_detail"),
    path(_('sponsorship/<slug:slug>/'), SponsorshipDetailView.as_view(),
        name="sponsorship_detail"),

    path(_('news/<slug:slug>/'), NewsEntryDetailView.as_view(),
        name="news_detail"),
    path('<slug:slug>/', CommonDetailView.as_view(),
        name="common_detail"),
]
