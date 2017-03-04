from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    url(r'^api/', include('app.urls')),
    url(r'^', include('cauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', get_swagger_view(title='Project API')),
]
