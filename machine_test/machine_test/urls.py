from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),  # Your app's URLs
    path('', RedirectView.as_view(url='/admin/')),  # Redirect to admin panel
]

 