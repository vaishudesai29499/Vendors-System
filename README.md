# Description
This is a vendor management system task that involves creating, listing, updating, and deleting vendor details based on user input. 

Using the Django framework, I created a vendor app to display these details. 

Users can create vendors by providing various arguments, which are then stored in the backend database.

# Plan
- Start and Planning:Begin by comprehensively understanding the project scope and establishing the      foundational structure.

- Vendor Setup: Create a robust system for effectively managing vendor information and thoroughly test its functionality.

- Purchase Order Management: Develop purchase order forms and verify their functionality to ensure smooth transaction processes.

- Performance Evaluation: Implement a scoring mechanism for vendors and dynamically calculate their performance scores.

- Historical Tracking: Integrate a feature for tracking vendor performance history over time, enabling better decision-making.

- Testing Phase: Conduct rigorous testing to identify and rectify any issues or bugs present in the system.

- Deployment and Maintenance: Launch the system online for user accessibility and utilization.Continuously monitor the system, address any issues promptly, and provide ongoing support to users.

# Vendor Profile Management
- POST /api/vendors/: Create a new vendor.
- GET /api/vendors/: List all vendors.
- PUT /api/vendors/{vendor_id}/: Update a vendor's details.
- DELETE /api/vendors/{vendor_id}/: Delete a vendor.
- UPDATE /api/vendors/{vendor_id}/: Update a vendor.
- POST /api/contact/:Contact Us

# Purchase Order Tracking
 - POST /api/purchase_orders/: Create a new order.
 - GET /api/purchase_orders/: List all orders.
 - PUT /api/purchase_orders/{vendor_id}/: Update a order's details.
 - DELETE /api/purchase_orders/{vendor_id}/: Delete a order.
 - UPDATE /api/purchase_orders/{vendor_id}/: Update a order.

# Tech Components
Stack: Python3, Django, dbsqlite3

Server: localhost:8000


# Installation
```http

pip install django

pip install djangorestframework

pip install -r requirements.txt

python manage.py makemigrations 

python manage.py migrate

python manage.py createsuperuser 

python manage.py runserver

http://localhost:8000/vendors/  --for vendor list

http://localhost:8000/admin  --for admin
```

# Screenshots

#Homepage: The initial landing page of the website.
<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/9f58454c-5d57-4290-b14a-9b2f394c282f">
#Vendor Creation: Allows users to input basic details to create a vendor profile.
<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/01b64ddf-49b6-463b-a5e0-51a7a7ae7938">
#Vendor List Display: After adding a vendor, users can view a list of all vendors.
<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/cb0de1ab-d135-46aa-8473-ab1dcebc9ae5">
#Vendor Details Update: Users can update existing vendor details, and these changes are immediately reflected in the vendor list.
<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/7e7611da-6020-4d74-8e89-e5a7cee5f35b">
#Address Details Updated for the first vendor.
<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/a2451b7c-bee1-4656-b601-e0fe4dd40592">
#Vendor Deletion: To delete vendor details. Delete the 005 vendor with the changes reflected in the vendor list.
<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/f22492c7-2dc2-443a-b5b4-b04aa6d03302">
#Contact Us Form: A form where users can submit inquiries or messages to the website administrators.
<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/8238385b-591a-4b03-813d-ddaee2946adc">
# Administration Page:
   - Historical Performances: A section displaying historical performance data.
   - Purchase Orders: Information related to purchase orders.
   - Vendors: A section dedicated to managing vendor-related information.

<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/85f3092b-ac9a-40ff-b23f-244c4fb33bc4">
# Vendors List in Administration: Displays a list of vendors within the administration page, likely for management and oversight purposes.
<img width="1080" alt="image" src="https://github.com/vaishudesai29499/Vendors-System/assets/75478804/115532a0-ac61-4cd1-a213-b50ff763e933">
