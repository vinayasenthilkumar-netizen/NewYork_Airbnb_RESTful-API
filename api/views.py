# render used to retrun html template for the homepage 
from django.shortcuts import render
# ready made class based views 
from rest_framework import generics
# import the model 
from .models import AirbnbListing
from .serializers import AirbnbListingSerializer

from rest_framework import generics
# for api logic 
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
# average price 
from django.db.models import Avg

# homepage view to render html 
def HomePageView(request):
    return render(request, 'api/home.html')

# get all lstings and create a new listing 
class AirbnbListingList(generics.ListCreateAPIView):
    queryset = AirbnbListing.objects.all()
    serializer_class = AirbnbListingSerializer

# get by id , can update and even delete the listing 
class AirbnbListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AirbnbListing.objects.all()
    serializer_class = AirbnbListingSerializer
    lookup_field = 'id'

# listing by borough 
class ListingsByBorough(generics.ListAPIView):
    serializer_class = AirbnbListingSerializer

    def get_queryset(self):
        borough = self.kwargs['borough']
        return AirbnbListing.objects.filter(neighbourhood_group__iexact=borough)

# endpoint to filter by room type ( extra done just incase )
class ListingsByRoomType(generics.ListAPIView):
    serializer_class = AirbnbListingSerializer

    def get_queryset(self):
        room_type = self.kwargs['room_type']
        return AirbnbListing.objects.filter(room_type__iexact=room_type)

# endpoint to filter by under a particular price 
class ListingsUnderPrice(generics.ListAPIView):
    serializer_class = AirbnbListingSerializer

    def get_queryset(self):
        price = self.kwargs['price']
        return AirbnbListing.objects.filter(price__lte=price)

# endpoint to filter by the average pruce per borough ( extra done just incase )
class AveragePriceByBorough(APIView):
    def get(self, request):
        data = AirbnbListing.objects.values('neighbourhood_group').annotate(avg_price=Avg('price'))
        return Response(data)

# endpoint to filter by top reviewd listing ( extra done just incase )
class TopReviewedListings(APIView):
    def get(self, request):
        listings = AirbnbListing.objects.order_by('-number_of_reviews')[:10]
        serializer = AirbnbListingSerializer(listings, many=True)
        return Response(serializer.data)
# endpoint to filter by average price of a single borough ( extra done just incase )
class AveragePriceSingleBorough(APIView):
    def get(self, request, borough):
        data = AirbnbListing.objects.filter(
            neighbourhood_group__iexact=borough
        ).aggregate(avg_price=Avg('price'))
        return Response({"borough": borough, "avg_price": data['avg_price']})

# endpoint to filter by listing all the neighbourhoods available ( extra done just incase )
class NeighbourhoodList(APIView):
    def get(self, request):
        neighbourhoods = AirbnbListing.objects.values_list('neighbourhood', flat=True).distinct()
        return Response(sorted(neighbourhoods))
# # endpoint to filter by neighbourhood name  ( extra done just incase )
class ListingsByNeighbourhood(generics.ListAPIView):
    serializer_class = AirbnbListingSerializer

    def get_queryset(self):
        neighbourhood = self.kwargs['neighbourhood']
        return AirbnbListing.objects.filter(neighbourhood__iexact=neighbourhood)


