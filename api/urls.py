# import path used to define the url patterns in django 
from django.urls import path

# import all the view classes that handles the api request
from .views import AirbnbListingList
from .views import AirbnbListingDetail
from .views import ListingsByBorough
from .views import ListingsByRoomType
from .views import ListingsUnderPrice
from .views import AveragePriceByBorough
from .views import TopReviewedListings
from .views import AveragePriceSingleBorough
from .views import NeighbourhoodList
from .views import ListingsByNeighbourhood


# urlpatterns map the url paths to the correct views 
urlpatterns = [
    # endpoint for listing all the airbnb or creating a new one 
    path('listings/', AirbnbListingList.as_view(), name='listings-list'),
    # endpoint for updating retirving and deleting by listing id 
    path('listings/<int:id>/', AirbnbListingDetail.as_view(), name='listing-detail'),
    # endpoint to filter listings by borough
    path('listings/borough/<str:borough>/', ListingsByBorough.as_view(), name='listings-borough'),
    # endpoint to filter listing by under a particular price 
    path('listings/under-price/<int:price>/', ListingsUnderPrice.as_view(), name='listings-under-price'),
    # endpoint to filter listing by room type
    path('listings/room/<str:room_type>/', ListingsByRoomType.as_view(), name='listings-room'),
    # endpoint to filter listing by average price of a borough grouped by borough
    path('listings/avg-price/', AveragePriceByBorough.as_view(), name='avg-price'),
    # endpoint to filter listing by top reviewed listing 
    path('listings/top-reviewed/', TopReviewedListings.as_view(), name='top-reviewed'),
    # endpoint to filter listing by average price of 1 borough
    path('listings/avg-price/<str:borough>/', AveragePriceSingleBorough.as_view(), name='avg-price-single'),
    # endpoint to filter listing by listing all the neighbourhoods 
    path('listings/neighbourhoods/', NeighbourhoodList.as_view(), name='neighbourhood-list'),
    # endpoint to filter listing by a neighbourhood
    path('listings/neighbourhood/<str:neighbourhood>/', ListingsByNeighbourhood.as_view(), name='listings-neighbourhood'),
    
]
