from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import landing_page, home_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('reviews/', home_page, name='home'),
    path('users/', include("users.urls")),
    path('books/', include("books.urls")),
    path('api/', include("api.urls")),

    path('api-auth/', include('rest_framework.urls')),
    path('mankuadmin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)