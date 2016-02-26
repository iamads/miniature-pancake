from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fulfil.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'expensemanager.views.dashboard', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^expensemanager/', include('expensemanager.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
