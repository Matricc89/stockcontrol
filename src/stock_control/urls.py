
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compra/', include('compra.urls', namespace='compra'))
]
