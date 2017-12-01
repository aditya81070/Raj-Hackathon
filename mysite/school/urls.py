from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$',views.school_details,name='school_details'),
]