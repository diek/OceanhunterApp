from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('accounts.urls')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^privacy-policy$', 'pages.views.page', {'slug': 'privacy-policy'}, name='privacy-policy'),
    url(r'^rules-conditions$', 'pages.views.page', {'slug': 'rules-conditions'}, name='rules-conditions'),
    url(r'', include('main.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)


#urlpatterns += patterns('',
    #url(r'', include('pages.urls')),
#)
