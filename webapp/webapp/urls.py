from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bubble/', include('bubble.urls')),
    path('admin/', admin.site.urls),
]
