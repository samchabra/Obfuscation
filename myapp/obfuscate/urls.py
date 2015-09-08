from django.conf.urls import patterns, include, url

urlpatterns = patterns('obfuscate.views',
                       
    url(r'^$', 'index', name='home'),

    url(r'^(?P<obf_id>\w{36})$', 'redirectOriginal', name='redirectOriginal'),
                       
    url(r'^obfuscateLink/$', 'obfUrl', name='obfUrl'),

)
