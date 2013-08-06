from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^\d*$', 'treehole.views.index', name='index'), 
    url('^chart_day/', 'treehole.views.chart_day', name='chart_day'), 
    url('^chart_hour/', 'treehole.views.chart_hour', name='chart_hour'), 
    # Examples:
    # url(r'^$', 'treehole.views.home', name='home'),
    # url(r'^treehole/', include('treehole.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
