from faker import Faker
fake = Faker()
import random
from .models import *


def seed_db(n=10) -> None:
    try:
        for i in range(0,n):
          address=fake.address()
          vendor_code=random.randint(000,999)
          name=fake.name()
          contact_details=random.randint(1000000000,9999999999)
          name=fake.name()
          on_time_delivery_rate = random.randint(-4,4)
          quality_rating_avg = random.randint(-4,4)  
          average_response_time =random.randint(-4,4)  
          fulfillment_rate = random.randint(-4,4)  
          

          vendor_obj = Vendor.objects.create(
            address=address,
            vendor_code=vendor_code,
            name=name,
            contact_details=contact_details,
            on_time_delivery_rate =on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate

        )


    
        
    except Exception as e:
        print(e)