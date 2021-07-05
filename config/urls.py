from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("api/v1/", include("api.users.urls")),
    # Your stuff: custom urls includes go here
]
