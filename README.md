## MS4 - Old And Gold Vintage watch eCommerace
"header image"

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
4. As a user, I want it to be easy to contact the site owner. 
5. As a user, I want to be able to read more about the watches.  
6. As a user, I want to have a profile page that collect my recent purchases.

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





####   Upcoming Features
+ Buy watch straps 
+ The ability to add watches to a wishlist. 
+ More payment alternatives. 
+ Online auctions. 
+ More brands. 

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

# Deployment
## Heroku
## Amazon Web Services
## Local Deployment

# Credits   

### Images
- Thanks to Kaplans Auktioner in Sweden for letting me use their pictures in this project. <br>
- Hero picture from [Pexels](https://www.pexels.com/sv-se/foto/stad-gata-byggnad-hus-2309235/).

### Tutorials
A big guidance in this project has been Boutique Ado from Code Institute. 