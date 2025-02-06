"""
URL configuration for common project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


urlpatterns = [
    path("admin/", admin.site.urls),
    path('daialy/', include('daialy.urls')),
    path('pg003_query/', include('pg003_query.urls')),
    path('pg005_smarturl/',include('pg005_smarturl.urls')),
    path('pg006_urlcalc/',include('pg006_urlcalc.urls')),
    path('pg007_statictemp/',include('pg007_statictemp.urls')),
    path('pg008_dynamic/',include('pg008_dynamic.urls')),
    path('pg009_pagemove/',include('pg009_pagemove.urls'))
]
