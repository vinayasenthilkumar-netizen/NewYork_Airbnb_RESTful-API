"""
URL configuration for midterm_awd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# import admin interface 
from django.contrib import admin
# import path and include for the url routing
from django.urls import path, include
# import the homepage view 
from api.views import HomePageView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

# url configuration for the project 
urlpatterns = [
    # landing page for the application 
    path('', HomePageView, name='home'),      
    
    # admin interface panel 
    path('admin/', admin.site.urls),
    # include all the api 
    path('api/', include('api.urls')),

    # OpenAPI schema (machine-readable)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI (human-friendly)
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

