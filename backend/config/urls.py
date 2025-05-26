from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.job_seekers.views import JobApplyView


urlpatterns = [
    path("", include("common.urls"), name="common"),
    path("admin/", admin.site.urls, name="admin"),
    path("polls/", include("apps.polls.urls"), name="polls"),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)