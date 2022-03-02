from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
	path('ckeditor/', include('ckeditor_uploader.urls')),
] + i18n_patterns (
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('myblog.urls')),
    prefix_default_language=False
)