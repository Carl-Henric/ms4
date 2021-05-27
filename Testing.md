## Testing - Old And GOld - MS4

### Code validators
I have used  [WS3](https://jigsaw.w3.org/) validators for both html and css. 

#### Html:
Passed all tests. 
***

#### CSS:
Passed all tests. 
***

### Speed
![speed](/media/speed2.png "Speed")

The site speed is C which is ok. For better speed on the site, all images needs to be compressed for less weight. <br>
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

### Testing Enviroment
- All tested is done by me, and when external users needed, then my friends helped me with that. <br>
- Both desktop and mobile have been used within the tests, and Google dev tools.
- All pages and functions have been tested during the project with Google dev tools for direct response for any upcoming erros. 