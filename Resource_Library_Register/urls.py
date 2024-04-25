from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

urlpatterns = [
    path('', views.user_form,name='resource_insert'), #get and post req. for insert operation
    path('<int:id>/', views.user_form, name='resource_update'), #get and post req. for update operation
    path('delete/<int:id>/', views.user_delete, name='resource_delete'), 
    path('list/', views.user_list,name='user_list') #get req. to  retrieve and display all records
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
