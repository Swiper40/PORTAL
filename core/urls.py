
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from simple_multivendor_site.settings import MEDIA_ROOT, MEDIA_URL
from simple_multivendor_site.settings import DEBUG

from .views import Contact, Home

app_name = 'core'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contact/', Contact.as_view(), name='contact'),

]