## MS4 - Old And Gold Vintage watch eCommerace
![Header](/media/readmeheader.png "Home")

Old And Gold is my fictive webshop with handpicked exclusive vintage watches. Each watch is one of a kind and theres is only one of each watch. 
I wanted the site to be very straight forward with few categories and minimize objects that can distract the visitor form proceeding a purchase. 

The target audience is watch entusiasts that are seeking for a specific watch thar are hard to find. Old And Gold is only 
selling Rolex, Omega and Patek Phillipe beacuse they have the most strong purchase power audience. 

# Ux
 
## Strategy

The primary goal wiith this eCommerce is to have a small selection of unique vintage watches. The primary audience is watch enthusiasts that are looking for unique watches that are hard to get. 


### Business objective 
1. As a site owner, I want to offer a eCommerce that ensures that all payment is safe for all parts.
2. As a site owner, I want the visual impression to be serious and reliable. 
3. As a site owner, I want the user to know how to forward in the funnel in all steps until completed purchase. 
4. As a site owner, I want it to be easy for me as admin to add more products.

### User Stories 
1. As a user, I want to know how to proceed my purchase in all steps. 
2. As a user, I want it to be clearly what kind of watches the eCommerce offers. 
3. As a user, I want to feel secure with the payment. 
4. As a user, I want to be able to read more about the watches.  
5. As a user, I want to have a profile page that collect my recent purchases.
6. As a user, I want it to be easy to find all the products. 

## Scope
The site is build to have a light but serious touch. It should be easy for the user to see what watches there is in stock. I wanted the site to be serious but not too stiff and boring, and wioth a small touch on vintage boutique. 


### Features
#### Current Features
+ Navigaton bar on desktop
+ Hamburger navigation-menu on mobile devices
+ Shopping cart in header visible on all pages and all devices. 
+ Profile icon/link in header on desktop visible on all pages.  
+ Profile icon/link in hamnburger menu  on mobile devices. 
+ Profile icon/link in header on desktop visible on all pages.  
+ Categories for Rolex, Omega, Patek Philippe and All watches.
+ Add watch to shopping bag.
+ Delete a watch from shopping bag.
+ Form with buyer/shipping details in checkoput. 
+ Complete checkout funcktionality. 
+ Secure payment with Stripe. 
+ Profile page with saved information. 
+ As admin, the ability to add a product. 
+ Confirmation mail when purchase is completed. 
+ When a watch is purchased it removes from the shop. 



####   Upcoming Features
+ Buy watch straps 
+ The ability to add watches to a wishlist. 
+ More payment alternatives. 
+ Online auctions. 
+ More brands. 
+ Compress all the images. 
+ Add footer.
+ Complete email confirmation functionality. 


## Structure
The site consists of:
+ **Home**

    Introduce the concept of Old & Gold for the first time visitor and what to expect for the visit. 
    Helps the user forward in to the site.  
    ***
+ **Categories** (All watches, Rolex, Omega and Patek Philippe)
 
    There is four categories where the watches is displayed. Due to the small assortment I wanted to keep it easy for the user to find the watches. 
    I kept the categories linked to the brand and not to the uses for the watch. 
    ***
+ **Product detail**

    The product detail page displays all the info about each watch. I wanted the info about each watch to be shorthanded and easy to understand but with all the required info clear to the user. 
    The most important info for a vintage watch is year, condition and price. 
    ***
    
+ **Shopping bag**
    
    The most relevant information is displayed in the shopping bag, and the total amount. The possibillity exists to remove product from cart, and return to all watches. 
    ***
+ **Checkout**

    Crispy forms form with all personal and shipping details is displayed. Stripe payment with webhooks is used to secure the checkout process. 
    ***
+ **Checkout success**

    The user redirects to a checkout success page where  the user information is stored and displayed to the customer. 
    ***
+ **Profile**

    The profile page stores the user information and order history for the user. 
    ***
+ **Product management** (For Admin/Superuser)

    The product management page makes is poissible for the admin to add more products to the shop. 
    ***


## Skeleton
### Wireframes

**Home**
 ![Home](/media/wireframes/home.png "Home")
 ***
 **Products**
 ![Products](/media/wireframes/products.png "Products")
 ***
 **Details**
 ![Details](/media/wireframes/details.png "Details")
 ***
 **Cart**
 ![Cart](/media/wireframes/cart.png "Cart")
 ***
 **Checkout**
 ![Checkout](/media/wireframes/checkout.png "Checkout")
 ***
 **Checkout success**
 ![Checkout Success](/media/wireframes/confirmation.png "Checkout success")
 ***
 **Profile**
 ![Profile](/media/wireframes/profile.png "Profile")
 ***

## Surface
My main goal with the design was to make the homepage feel serious with a glimpse of vintage. The products in the shop so the overall feeling of the site has to be confidence-inspiring.

### Design 

The main reason for the visitors are to see the watches, so all images are in big sizes and the information about the watches are more laidback. 
#### Colours
The main theme of the colours are off white, blue grey, dark grey and orange. See picture below:<br>
 ![Colors](/media/colours.png "Colours"). <br>
 Color scheme comes from [color hunt](https://colorhunt.co/palette/264862) 
 ***

#### Fonts

The fonts that have been used comes from [Google fonts](https://fonts.google.com/).<br>
**Headings**: Satisfy<br>
**Paragraphs/buttons**: Roboto Condensed
*** 
#### Images 
All product images are big and crispy and really shows the beuty in every watch. For such a visually beautiful product, images are required that highlights it.
***
#### Icons
All icons on the site comes from  [Font Awesome](https://fontawesome.com/).
***


# Information Architecture 
## Database Choice
Under the development part, the default Django SQLight database where used. And in the deplyment part, the Heroku Add-on PostgreSQL where used. 
## Data modelling  
Categories and Products have been used as fixtures and are in Json format. 
![schema](/media/schema.png "db schema")
# Accessability
## alt-tags on images
For accessability have alt-tags been implemented on all images. Partly because of the user-friendliness for the visually impaired and partly for Google indexing the page. 
# Technologies used
## Languages used  
- HTML 
- CSS
- Javascript
- Python

## Frameworks used
- Boootstrap
- Django
- jQuery  

## Storage/Database
- Django SQLight (database under the development part, before deployment to Heroku) 
- Heroku PostgreSQL (database)
- Aamazon Web Services (storing static and media files)

## Storing, editing and deploying
- Gitpod
- Github
- Heroku

## Other
- Stripe Payments
- Django Allauth
- Django Crispy forms 
- Balsamiq
- Beutifier

# Testing  
### Code validators
I have used [WS3](https://jigsaw.w3.org/) validators for both html and css. 

#### Html:
Passed all tests. 
***

#### CSS:
Passed all tests. 
***

### Speed
![speed](/media/speed2.png "Speed")

The site speed is C which is ok. For better speed on the site, all images needs to be compressed for less weight. The can be more developed for faster loading. <br>
The lack of time in the project had me to skip that. But it will be fix in future fixes.  

### User Stories
| As a/an        | I want/need to           | Testing  | Result  |
| ------------- |-------------| -----|-----|
| **Site Owner**    | to offer a eCommerce that ensures that all payment is safe for all parts. | Payment with Stripe and webhooks | Works as expected, Stripe collect all the transers and the order stored in the db.   |
| **Site Owner**    | the visual impression to be serious and reliable.  | Have been tested it on some friends | The overall impression is good. |
| **Site Owner**    | I want the user to know how to forward in the funnel in all steps until completed purchase. | There are contrasting buttons to help the user forward the funnel. Some firends tested to proceed a purchase. | works as expected, no misunderstandings.  |
| **Site Owner**    | I want it to be easy for me as admin to add more products. | Tested added products via product management | Works as expected, products adds to the shop. |
| **User**    | to know how to proceed my purchase in all steps. | Some friends tested to buy a watch without any instructions. |Works as expected, its all clearly what to do. |
| **User**    | it to be clearly what kind of watches the eCommerce offers. | Made four nav items, for all watches, Rolex, Omega and Patek | all watches displays clearly in the categories |
| **User**    | to feel secure with the payment. | Stripe is used for secure payments |Works as expected, everything works. |
| **User**    | to be able to read more about the watches. | Product detail pages on all products |Works as expected, products details works fine. |
| **User**    | to have a profile page that collect my recent purchases. | all registrated users have a profile page |Works as expected, all info saves and displays in profile. |
| **User**    | it to be easy to find all the products. | All watches in menu displays all the products. |Works as expected, all watches shows. |

***

### Features
+ Navigaton bar on desktop
    - Shows in all browsers.
+ Hamburger navigation-menu on mobile devices
    - Displays and works on all mobile devices I have tested on with Google devolper tools. 
+ Shopping cart in header visible on all pages and all devices. 
    - Visible on all pages and on all devices within Google dev tools.
+ Profile icon/link in header on desktop visible on all pages.  
    - Visible on all pages.
+ Profile icon/link in hamnburger menu on mobile devices. 
    - Displays and works correct. 
+ Profile icon/link in header on desktop visible on all pages.  
    - Displays and works correct.
+ Categories for Rolex, Omega, Patek Philippe and All watches.
    - Displays and works correct. 
+ Add watch to shopping bag.
    - Works correct.
+ Delete a watch from shopping bag.
    - Works correct, watch removes fom bag. 
+ Form with buyer/shipping details in checkoput. 
    - Displays and works correct. 
+ Complete checkout functionality. 
    - Works correct and remove purchased watch from the store. 
+ Secure payment with Stripe. 
    - Works correct without any errors. 
+ Profile page with saved information. 
    - Works correct, all relevant data for the user is stored. 
+ As admin, the ability to add a product. 
    - Works correct from product management page. 
+ Confirmation mail when purchase is completed. 
    - Works almost. The functionality is done but the smpt server isen´t correclty setup. 
+ When a watch is purchased it removes from the shop. 
    - Works correct, when a watch is purchased it´s not longer aviable in the shop.

### Testing Enviroment
- All tested is done by me, and when external users needed, then my friends helped me with that. <br>
- Both desktop and mobile have been used within the tests, and Google dev tools.
- All pages and functions have been tested during the project with Google dev tools for direct response for any upcoming erros. 

# Deployment
## Heroku
For deployment to Heroku, there is some steps you had to proceed to finally visiting your page. 
When deploying this project to Heroku, following steps needed to be made. 
1. Log in to Heroku and create a new app, called oldandgod. 
2. Added PostgreSQL to my Heroku app with free license.
3. At settings, reveal config vars. 
    > **AWS_ACCESS_KEY_ID**: Your AWS Access key<br>
    > **AWS_SECRET_ACCESS_KEY**: Your AWS Secret Access key<br>
    > **DATABASE_URL**: Your PostgreSQL url<br>
    > **SECRET_KEY**: Your Django secret key<br>
    > **STRIPE_PUBLIC_KEY**: Your Stripe public key<br>
    > **STRIPE_SECRET_KEY**: Your Stripe secret key<br>
    > **STRIPE_WH_SECRET**: Your Stripe WH key<br>
    > **USE_AWS**: True<br>
    
4. Open Gitpod. 
5. Install guniron, psycopg2-binary and dj-database-url using pip3 install [name]. 
6. Store them into requirements.txt with *pip3 freeze > requirements.tx*t. 
7. Create a Procfile with the name of Procfile.py with *web: gunicorn oldandgold.wsgi:application* in it. 
8. Push changes to github.
9. For automatic deployment, go to deploy and connect to Githib and Enable automatic deploy.
10. In settings.py, comment out
```
    > DATABASES = {     
        'default': dj_database_url.parse("<Postrgres database URL>")     
    }
``` 
11. Makemigrations and migrate in the terminal to migrate to PostgreSQL.
12. In the terminal: 
    *python3 manage.py loaddata categories* <br>
    *python3 manage.py loaddata products*
13. Create a superuser in the terminal: *python3 manage.py createsuperuser*
14. In settings.py, replace the code so the correct database is used depending on the enviroment. <br>
    ```
     if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
15. In the terminal, *heroku config:set DISABLE_COLLECTSTATIC=1* (or add in in on Herok settings page).
16. In settings.py, add *ALLOWED_HOSTS = ['oldandgold.herokuapp.com', 'localhost']*
17. Go to Stripe > devolpers > webhooks. And set *https://oldandgold.herokuapp.com/checkout/wh/* as the new webhook url. 
18. Go to Settings.py and update Stripe enviroment variables, and finally. 
19. Push to Heroku and check build log that everything seems to be ok. 

## Amazon Web Services
For hosting static and media files, AWS have been used. Tha core is to create bucket where yuor files are stored in.
1. Go to Amazon Web Services. 
2. Create a bucket in S3 with static website hosting. Paste in the following code under permissions.
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
] 
```
3. Create a security policy to the bucket. 
4. Create a user with IAM
5. Create a group and attatch our policy to it. 
6. Create a user and add it to the group and download the .csv file with your user access key and secret access key in it. 
7. Go to Django and in the terminal, enter *pip3 install boto3* and *pip3 install django-storages*
8. Add your installed packages to requirements with *pip3 freeze > requirements.txt* 
9. In settings.py, add storages to your installed apps.
10. Go to Heroku and settings and add the keys from the .csv you download from AWS. 
11. Add USE_AWS as key with True as value, and remove collecstatic variable. 
12. Create a file called custom_storages.py and add this:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
13. In settings.py, Django need to know where to find our static files from now on.
```
if 'USE_AWS' in os.environ:
    # AWS BUCKET CONFIG
    AWS_STORAGE_BUCKET_NAME = 'oldandgold'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # STATIC AND MEDIA FILES
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # OVERIDE STATIC AND MEDIA URL´s In PRODUCTION
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
14. Push to Github, and Heroku beacuse the automatic deploy is enabled. 
15. Voila!


## Github
This project is stored at Github and can easliy cloned and further developed.
1. Got to Github and search for Carl-Henric or click here [here](https://github.com/Carl-Henric/ms4).
2. Press the **Code** button and copy the link. 
3. In Gitpod, in the terminal, type *git clone [paste in copied url]*.
4. Add env.py to store veriables and check your .gitignore file the env.py includes in it.   


# Credits   

### Images
- Thanks to Kaplans Auktioner in Sweden for letting me use their pictures in this project. <br>
- Hero picture from [Pexels](https://www.pexels.com/sv-se/foto/stad-gata-byggnad-hus-2309235/).

### Tutorials
A big guidance in this project has been Boutique Ado from Code Institute. 