from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Incubator.views.home', name='home'),
    url(r'^measures$', 'Incubator.views.measures', name='measures'),
    url(r'^lights/(?P<light_number>\w+)/(?P<command>\w+)/$', 'Incubator.views.lights', name='lights'),
    url(r'^new_hatching', 'Incubator.views.new_hatching', name='new_hatching'),
    url(r'^temperatures', 'Incubator.views.temperatures', name='temperatures'),
    url(r'^humidities', 'Incubator.views.humidities', name='humidities'),
    url(r'^retrieve_image/(?P<cam_number>\w+)/$', 'Incubator.views.retrieve_image', name='retrieve_image'),
    url(r'^show_more/(?P<cam_number>\w+)/$', 'Incubator.views.show_more', name='show_more'),
    #url(r'^take_picture/(?P<light_number>\w+)/$', 'Incubator.views.take_picture', name='take_picture'),
    # url(r'^Incubator/', include('Incubator.foo.urls')),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    #url(r'^accounts/logout/','django.contrib.auth.views.logout', {'template_name': 'cuentas_X/logged_out_bootstrapped.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),
	#url(r'^(?P<nombre>[\w|\W]+)/$', views.CV, name='CV'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
