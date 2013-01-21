from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Project
    url(r'^$', 'faraja.website.views.index', name='index'),
    url(r'^who_we_are$', 'faraja.website.views.who_we_are', name='who_we_are'),
    url(r'^trustees$', 'faraja.website.views.trustees', name='trustees'),
    url(r'^what_we_do$', 'faraja.website.views.what_we_do', name='what_we_do'),
    url(r'^activity/(?P<id_activity>[0-9]+)/$', 'faraja.website.views.activity', name='activity'),
    url(r'^therapists$', 'faraja.website.views.therapists', name='therapists'),
    url(r'^involved$', 'faraja.website.views.involved', name='involved'),
    url(r'^cancer$', 'faraja.website.views.cancer', name='cancer'),
    url(r'^testimonials$', 'faraja.website.views.testimonials', name='testimonials'),
    url(r'^faq$', 'faraja.website.views.faq', name='faq'),
    url(r'^contact_us$', 'faraja.website.views.contact_us', name='contact_us'),
    url(r'^donate$', 'faraja.website.views.donate', name='donate'),
    url(r'^news$', 'faraja.website.views.news', name='news'),
    url(r'^detail_news/(?P<id_news>[0-9]+)/$', 'faraja.website.views.detail_news', name='detail_news'),
    
    #Widgets
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^faraja/', include('faraja.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
