from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from . import settings

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('pages.urls')), 

# User management
path('accounts/', include('allauth.urls')), # new
# Local apps
path('accounts/', include('users.urls')),
path('services/', include('services.urls')),
path('shopping/',include('store.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
