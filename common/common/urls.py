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
    path('pg009_pagemove/',include('pg009_pagemove.urls')),
    path('pg010_css/',include('pg010_css.urls')),
    path('pg011_boot_strap/',include('pg011_boot_strap.urls')),
    path('pg012_post/',include('pg012_post.urls')),
    path('pg013_makeview/',include('pg013_makeview.urls')),
    path('pg014_get_post_view/',include('pg014_get_post_view.urls')),
    path('pg015_form_class/',include('pg015_form_class.urls')),
    path('pg016_as_table/',include('pg016_as_table.urls')),
    path('pg017_form_bootstrap/',include('pg017_form_bootstrap.urls')),
    path('pg018_view_class/',include('pg018_view_class.urls')),
    path('pg019_maxlength/',include('pg019_maxlength.urls')),
    path('pg020_freespace/',include('pg020_freespace.urls')),
    path('pg021_email_input/',include('pg021_email_input.urls')),
    path('pg022_float_input/',include('pg022_float_input.urls')),
    path('pg023_date/',include('pg023_date.urls')),
    path('pg024_strtofloat/',include('pg024_strtofloat.urls')),
    path('pg025_numeric_only/',include('pg025_numeric_only.urls')),
    path('pg026_checkbox/',include('pg026_checkbox.urls')),
    path('pg027_yesno/',include('pg027_yesno.urls')),
    path('pg028_choice/',include('pg028_choice.urls')),
    path('pg029_radiobutton/',include('pg029_radiobutton.urls'))
    ]


