from django.conf.urls import include, url
from django.contrib import admin
from gettingstarted import views

from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.urls import path
admin.autodiscover()

# import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', views.login_redirect, name = 'login_redirect'),
    url(r'^saferdb/', include('saferdb.urls', namespace='saferdb')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts') ),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name = 'password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),

]
