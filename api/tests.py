# apitestcase give test 
from rest_framework.test import APITestCase
# status code like 404 and all that
from rest_framework import status
# import the model to create test data and check the database 
from api.models import AirbnbListing


class AirbnbListingAPITests(APITestCase):
    def setUp(self):
        # create a listing for the test 
        self.listing = AirbnbListing.objects.create(
            name="Test Listing",
            host_name="Emily",
            neighbourhood_group="Brooklyn",
            neighbourhood="Williamsburg",
            room_type="Private room",
            price=120,
            minimum_nights=2,
            number_of_reviews=10,
            availability_365=200,
        )

    #  GET /api/listings/  returns all listings 
    def test_get_all_listings(self):
        response = self.client.get("/api/listings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    # POST /api/listings/ create a new listing using post
    def test_create_listing(self):
        payload = {
            "name": "New Listing",
            "host_name": "John",
            "neighbourhood_group": "Manhattan",
            "neighbourhood": "Harlem",
            "room_type": "Entire home/apt",
            "price": 150,
            "minimum_nights": 3,
            "number_of_reviews": 0,
            "availability_365": 300,
        }

        response = self.client.post("/api/listings/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AirbnbListing.objects.count(), 2)
        self.assertIn("id", response.data) 

    # GET /api/listings/<id>/ ( retun by the id)
    def test_get_single_listing(self):
        response = self.client.get(f"/api/listings/{self.listing.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.listing.id)
        self.assertEqual(response.data["host_name"], "Emily")

    # PUT /api/listings/<id>/  (update) test the updating of the listing 
    def test_update_listing_put(self):
        payload = {
            "name": "Updated Listing Name",
            "host_name": "Emily",
            "neighbourhood_group": "Brooklyn",
            "neighbourhood": "Williamsburg",
            "room_type": "Private room",
            "price": 99,
            "minimum_nights": 2,
            "number_of_reviews": 10,
            "availability_365": 200,
        }

        response = self.client.put(f"/api/listings/{self.listing.id}/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.listing.refresh_from_db()
        self.assertEqual(self.listing.price, 99)
        self.assertEqual(self.listing.name, "Updated Listing Name")

    # DELETE /api/listings/<id>/  test the deleting of the listing 
    def test_delete_listing(self):
        response = self.client.delete(f"/api/listings/{self.listing.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AirbnbListing.objects.count(), 0)

    # GET /api/listings/borough/<borough>/ test 1 endpoint filter by borough
    def test_listings_by_borough(self):
        response = self.client.get("/api/listings/borough/Brooklyn/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
        data = response.data
        if isinstance(data, dict) and "results" in data:
            data = data["results"]
        # makes sure that a list of the listing is seen
        self.assertIsInstance(data, list)
        # make sure atleast one id matches the one that was created
        self.assertTrue(any(item["id"] == self.listing.id for item in data))

        # GET /api/listings/under-price/<price>/ test the filter by max price
    def test_listings_under_price(self):
        response = self.client.get("/api/listings/under-price/150/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        if isinstance(data, dict) and "results" in data:
            data = data["results"]

        self.assertIsInstance(data, list)
        # check that returned listings have price <= 150
        self.assertTrue(all(item["price"] <= 150 for item in data))
        # test listing (price=120) should appear in the results
        self.assertTrue(any(item["id"] == self.listing.id for item in data))
