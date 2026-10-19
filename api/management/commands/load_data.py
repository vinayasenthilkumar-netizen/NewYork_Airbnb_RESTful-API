
# basecommand to create custom django management command
from django.core.management.base import BaseCommand
# read and work with the csv
import pandas as pd
# import the AirbnbListing model to insert the data into the databse 
from api.models import AirbnbListing

class Command(BaseCommand):
    # description will be shown to tell user 
    help = 'Load the Airbnb CSV data into the database'

    def handle(self, *args, **options):
        # read clean csv
        df = pd.read_csv('data/airbnbtest_cleaned.csv')
        # go through each row in the dataframe
        for _, row in df.iterrows():

            # create airbnb listing object for every row 
            # each field is mapped to the column in the csv
            AirbnbListing.objects.create(
                name=row['name'],
                host_name=row['host_name'],
                neighbourhood_group=row['neighbourhood_group'],
                neighbourhood=row['neighbourhood'],
                room_type=row['room_type'],
                price=int(row['price']),
                minimum_nights=int(row['minimum_nights']),
                number_of_reviews=int(row['number_of_reviews']),
                availability_365=int(row['availability_365']),
            )

        self.stdout.write(
            self.style.SUCCESS('CSV data loaded successfully!')
        )
