from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('Resource_Library_Register.urls'))
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
