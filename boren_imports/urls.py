from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('core.urls')),
    path("services/", include('services.urls')),
    path("auth/", include('user_authentication.urls')),
    path("newsletter/", include('newsletter.urls')),

    #wagtail urls
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),

    #broswer reload url
    path("__reload__/", include("django_browser_reload.urls")),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
