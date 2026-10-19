from django.apps import AppConfig


class ApiConfig(AppConfig):
    # internal name of the app which matches the folder name 
    name = 'api'
    # how the app name appears in the admin interface 
    verbose_name = "Airbnb in NY"
