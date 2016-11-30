from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from nabes_app.views import (IndexView, NewsletterListView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^newsletter/$', NewsletterListView.as_view(), name='newsletter_listview'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
