from django.conf.urls import url , include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^todo/', include("todo.urls")),
    url('^', include("myblog.urls")),
    url('^', include("users.urls")),

]

