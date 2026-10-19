# import models module to define the database tables 
from django.db import models
# model showing how one AirbnbListing showuld be 
class AirbnbListing(models.Model):
    # store the fields according to how it should be stored in the databse 
    name = models.CharField(max_length=255)
    host_name = models.CharField(max_length=100)
    neighbourhood_group = models.CharField(max_length=50)
    neighbourhood = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50)
    price = models.IntegerField()
    minimum_nights = models.IntegerField()
    number_of_reviews = models.IntegerField()
    availability_365 = models.IntegerField()

    class Meta:
        # model name 
        verbose_name_plural = "Airbnb"
    # show useful information like name of the airbnb and the bourough
    def __str__(self):
        return f"{self.name} ({self.neighbourhood_group})"
