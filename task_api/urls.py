"""
URL configuration for task_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_app import router as user_router
from house_app import router as house_router
from django.conf import settings
from django.conf.urls.static import static

auth_urls = [
    path(r'', include('drf_social_oauth2.urls'),),
]

if settings.DEBUG:
    auth_urls.append(path(r'verify/', include('rest_framework.urls')))

user_url_pattern = [
    path(r'auth/', include(auth_urls)),
    path(r'account/', include(user_router.router.urls)),
    path(r'main/', include(house_router.router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(user_url_pattern)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
