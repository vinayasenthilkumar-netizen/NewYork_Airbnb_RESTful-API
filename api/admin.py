
# import django admin module (to manage models through the admin panel)
from django.contrib import admin
# import AirbnbListing model 
from .models import AirbnbListing

# register the models  (django admin interface )
@admin.register(AirbnbListing)
class AirbnbListingAdmin(admin.ModelAdmin):
   # list the display controls ( fields as the columns )
    list_display = ('name','host_name', 'room_type','neighbourhood_group','neighbourhood','minimum_nights','number_of_reviews', 'price','availability_365',)
    # key word based seraching in the admin panel 
    search_fields = ('name', 'host_name','room_type','neighbourhood_group','number_of_reviews', 'price') # give results based on keyword
 



