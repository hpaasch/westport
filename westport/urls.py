from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout


from nabes_app.views import (IndexView, NewsletterListView, CreateAccountView,
ProfileView, ProfileUpdateView, LeadershipListView, DirectoryListView, StreetListView,
directory_printed)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout, name='logout'),
    url(r'^create_account/$', CreateAccountView.as_view(), name='create_account_view'),
    url(r'accounts/profile/$', ProfileView.as_view(), name='profile_view'),
    url(r'accounts/profile/update/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^newsletter/$', NewsletterListView.as_view(), name='newsletter_listview'),
    url(r'^leadership/$', LeadershipListView.as_view(), name='leadership_listview'),
    url(r'^directory/$', DirectoryListView.as_view(), name='directory_listview'),
    url(r'^streets/$', StreetListView.as_view(), name='street_listview'),
    url(r'^pdf/$', directory_printed, name='pdf_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
