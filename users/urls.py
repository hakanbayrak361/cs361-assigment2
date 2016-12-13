from django.conf.urls import url, include

from .views import signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^users/register/$', signup),
    url(r'', include("django.contrib.auth.urls"))

]
