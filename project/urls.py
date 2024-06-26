
from django.contrib import admin
from django.urls import path,include
from app.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('account/', include('account_app.urls')),
    path('create/', include('post_app.urls')),
]
