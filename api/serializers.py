# import serializers ( convert model objects to json)
from rest_framework import serializers
from .models import AirbnbListing
# defines how the airbnb listing object is shown through the api 
class AirbnbListingSerializer(serializers.ModelSerializer):

    class Meta:
        # model
        model = AirbnbListing
        # include all fields from the model
        fields = '__all__'  
       
