import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('baskets/', include('basketapp.urls', namespace='baskets')),
    path('admin-staff/', include('adminapp.urls', namespace='admins'))
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
