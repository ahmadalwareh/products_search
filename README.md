# Products Search
## A techincal task working on for Real estate company

Create a new Python Django project that contains the following:
Implement a feature that allows users to search for products based on category and price range and retrieve the matching products along with their respective details, with authentication using JWT and data stored in a MySQL database.


1.	Create a new endpoint in the "products" app that will handle the GET request to search for products, which requires authentication using JWT
2.	Implement a new serializer class in the "serializers.py" file of the "products" app that will handle the search criteria, such as:
•	category (CharField)
•	brand (CharField)
•	min_price (DecimalField)
•	max_price (DecimalField)
•	min_quantity (IntegerField)
•	max_quantity (IntegerField)
•	created_at (DateTimeField)
3.	Create a new view in the "views.py" file of the "products" app that will handle the GET request to search for products and check for the user's authentication using JWT.
4.	Modify the existing "Product" model to include additional fields that will be used for searching, such as: rating (FloatField)
5.	Create a new URL pattern in the "urls.py" file of the "products" app that maps the GET request to the appropriate view.
6.	Configure the project to use a MySQL database and update the models to work with the new database.
7.	Test the new endpoint by sending a GET request to the endpoint with different search criteria and ensuring that the correct list of matching products is returned in the response after providing a valid JWT token.
8.	Create a cart model and cart view that allows users to add products to the cart, update and remove items from the cart, and also to view the cart.
9.	Implement pagination for the search results.
10.	Implement sorting for the search results.
11.	Use Swagger as API documentation.
12.	Implement image upload using multithreading or multiprocessing: 
a)	Modify the existing "Product" model to include an image field for product images. 
b)	Add a new endpoint in the "products" app that will handle the POST request for uploading a new product image. 
c)	Implement a new view that will handle the POST request, validate the incoming image data, and store the image in the database. 
d)	Utilize multithreading or multiprocessing to process the uploaded images in parallel, improving the performance of the image processing system. 
e)	Implement a task to generate different sizes of the same image for various use-cases (e.g. thumbnails, full-size images).
f)	Connect the image processing task to the image upload process so that the processing happens automatically whenever a new image is uploaded. 
g)	Test the implementation by uploading test images and verifying that the correct resized images are generated and stored.
13.	Use Celery to send an email to new users after 1 day of registration. 
a)	Integrate Celery into the Django project to handle background tasks such as sending emails. 
b)	Create a Celery task that will send an email to new users after 1 day of registration. The email should contain a personalized message and any relevant information about the website. 
c)	Schedule the Celery task to run after a specified interval of time, in this case, 1 day. 
d)	Test the implementation by registering a new user and verifying that the email is sent after 1 day.
14.	Deploy the Django project on Docker and upload it to GitHub. 
a)	Package project as Docker container. 
b)	Create Dockerfile with dependencies, config, and environment variables. 
c)	Build and run containers using Docker.
d)	 Commit Dockerfile and all relevant files to the GitHub repo.
e)	 Push code to GitHub to make it publicly accessible.

