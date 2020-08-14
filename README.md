[![Build Status](https://travis-ci.org/Lemoenskil/E-commerce-webpage-staraid.svg?branch=master)](https://travis-ci.org/Lemoenskil/E-commerce-webpage-staraid)

# E-commerce-website-Staraid

This web application has been designed and built for the requirements of the "E-commerce-website" project of the Code Institute Full-Stack Software Development course.  It is intended to be used as a  e-commerce website where you can buy the product,
and  the process from order to shipment.  Which will include a chart, payment, shipping and for the future invoicing.   There will also be a support which will be for before and after sales.
Staraid is a auto guider that is used when you are tracking stars for astrophotography it is a highly technical product and is intended to make life easier for the not that technical or entered astrophotography.
As it is niche market mostly focus on hobbyist the website will need to have a lot of information on it.  They will also be searching for review or current users as it is a pricy product it will not be a impulse buy.
There will also be extra product available that the customer can buy that is needed for his setup and addons for StarAid.  For the future a blog will be place where the more experience customer can share his photo and give user tips new customer
in this to try  build a the brand name.  The website will also have a Facebook link where we will share system updates and happy customer blogs.  The website will also be use for support for current and prospective customer to contact Staraid.

The project can be viewed [at the Heroku hosted site](https://staraid-ecommerce.herokuapp.com/).

## Specification / Design

The e commerce website for staraid will focus on the main product which is the auto guider with a few addons that you can buy for the telescope setup.   The website main function is to have a medium to place a order and settle the payment.
A potential shopper can brows the web store to get information about the product and create a shopping chart  (information would be like question and answer and or the videos and reviews on the web site).
When the customer has made his d to buy the products he will need to sign in and create a profile to proceed with the order.  After registering he can proceed to choose the method of shipment which will add an extra amount to the total.
Then the customer can proceed the to the payment type (which for this website will be a credit card).
After the payment have been successful the customer will receive and invoice as a mail.(for future implementation)

The customer can use his profile to review and comment and rate the product.  (For the future I want a blog available where the customer can share his/her experience tell about his setup and condition and place a photo).
The home page will have a carousel where you can get a overview of picture and features,  a on offer area and an a featured product area with review will be available.  Also review on the on offer product will be available on the landing page.
Prospective customer can contact us via form (I will be looking at a chatbot for the future and  for customer who have order the product need to login that we have there product available and can be of better assistance
as for some instances they will need to add a error log).

The design of the website can been seen in more detail in the sitemap in mock-ups, but we will use a mostly white back ground with a bar of purple and blue simulating twilight. I will be using a bootstrap standard template.

In adding extra value added functionality in the future, I will be looking at tool and Api that can give weather pattern to when it will be a clear night for astrophotography also maybe adding best spot for astrophotography.
 
## UX
 
### Build Data E-commerce-website-Staraid

The E-commerce-website-Staraid has the following requirements

Their primary target audiences professional, hobbyist and starting astrophotography’s
The website need to include the following 
- Database with product, prices, stock, customer, photo's and review (see detailed database diagram)
- Ability to add new product to your shopping chart
- The ability to change existing shopping chart
- The ability to delete shopping chart
- View products
- Search for products
- View information ex Q&A, review 
- Browse the website with out signing in 
- Only user signed in can place order write a review and blog.(blogs are for future implementation)
- Register user: ability to change, (delete reviews and blogs is for future implementation)
- Photos and videos as information on the product 
- Have terms, conditions and policies 

I need the following for the website
- logo/ Name
- Data Base for product, prices, stock, review, b
- Picture, videos
- Bootstrap template
- Stripe setup
-

### Stakeholders

The following stakeholders will interact with the website:

* Customer
* Content Manager
* Accounting (future implementation)
* Fulfilment specialist (future implementation)
* Logistics

### User stories

#### View products

As a customer I would like to view a list of products so I can select some to purchase

Acceptance criteria:

* Can see an thumbnail image for each product
* Can click to view the details of the product
* Can add to cart from details page
* Can search for a product


#### Review a product

As a customer I would like to review a product so that I can share my experience

Acceptance criteria:

* Cannot review a product if not logged in
* Can click to add a review from the product details page
* Can select a rating from the review page
* Can enter a description of my experience
* Can submit my review
* Can update my review (future implementation)
* Can delete my review (future implementation)

#### Change Shopping chart

As a customer I want the ability to review my shopping chart to make changes to it

Acceptance criteria:

* View quantities and item in the chart
* See a total cost before tax and shipping
* Remove items
* Adjust quantities of items
* Click to navigate to an item detail page

#### Check out items

As a Customer I want to check out to get my products ship to me

Acceptance criteria:

* Trigger checkout from any page if there are items in the chart
* Need to sign in
* If not registered need to register a profile (to get shipping and payment details)
* Show total include tax and shipping before finalising 
* Show conformation messages after finalising.(future implementation)
* Verify payment via payment processor (future implementation)

#### Register

As a customer i want to register in order to review and order products.

Acceptance criteria:

* Create a profile with full name, email, phone number, physical address and birthdate
* Trigger register when checking out
* Give and option to sign in or register
* Show on the navbar that you are signed in
* Give option in the navbar to sign out

#### View my orders (future implementation)

As a customer I want to review my orders so I can see my order history

Acceptance criteria:

* View a list of open and completed orders
* See the status of the order
* Navigate to details of the order
* Include a tracking nr if the order is shipped but not delivered
* Contact customer service from the order detail page

#### Update Product

As a content manager  I want to updated the products so I can adjust our offering over time

Acceptance criteria:

* Add and remove products
* Modify product images

####  Order report (future implementation)

As a fulfilment officer I want to print a order report  prepare the order confirm the tracking nr back

Acceptance criteria:

* Print a report for all open orders
* Updating order with the tracking nr from the transporter

#### Order Analytics (future implementation)

As Account I want to see the order analytics and the revenue that I can track it against our goals.

Acceptance criteria:

* View dashboards with total order and euro count
* Adjust the range with options today, this month, last 30 days, last 90 days, a year
* See chart comparing order revenue with total cost per product

#### Stock update

As a logistics officer I want to have an overview/update on the stock levels

Acceptance criteria:

* Updated the stock levels of product
* View a list of backorders (future implementation)
* View a dashboard that give the stock level and the replenishment times (future implementation)

#### Customer support

As a customer I want to contact the supplier to get information or help

Acceptance criteria:

* Complete a E-mail form

#### Writing a review

As a customer I want to write a review or rate my experience with start aid

Acceptance criteria:

* Login as a customer
* Give a rating out of 5 (stars)
* Submit the written review
* Change the review (future implementation)
* Delete the review (future implementation)

#### Blog (future implementation)

As a customer I want to write a blog about astrophotography and how staraid has improved my experience

Acceptance criteria:

* Login as a customer
* Post the text
* Add photo's
* Change blog
* Delete the blog
* Geo tag setup
* And select from a list telescope setup

#### Profile (future implementation)

As a customer I want to have insight in to mystaarid profile to update and see software updates

Acceptance criteria:

* Update full name, email, phone number, physical address and birthdate
* View order history
* View new software updates available
* View your blog and reviews
* See photo’s placed

#### News letter

As a customer or potential customer I want to subscribe to a newsletter

Acceptance criteria:

* Sign up for news letter
* Stop receiving newsletter


## Project Purpose

I am creating a website aimed towards current and prospective astrophotography’s in search of a multifunctional easy to use auto guider for their telescope setup. 
The website will be for the primary purpose to sell the product and secondary to support and nice to have the blog and extra user information.  
The website will be to guide the potential buyer in to buying the product by giving enough information an the ability for extra enquiry.
As a business owner this website will be use to support current customer and to keep contact with them, the reason to get information to improve the product and user experience.
For the business this website will be of value as it is our cash register for receiving money, keeping track of stock and issuing invoices
  
### Scope of website
- A Responsive website (mobile and desktop)
- Landing page with product introduction and reviews
- Product view page with detail information
- Product search functionality
- Logon ability for a user
- Chart functionality
- Check out functionality which include payment and shipment
- Review functionality
- Blog post (for the future)
- Customer profile
- Order overview for Customer service
- Stock overview for Logistics
- Customer communication via email or user account


### Website Structure

#### Database design for e-commerce website

![Database](/doc/staraid_db_webpage.png)

#### Site Map for e-commerce website

![Site Map](/doc/sitemap_staraid_new.png)                

### Mock-up’s

In the links below you can see the mock-up’s that I drew using the mock-up tool “Pencil”:
- Desk Top

![Desk top mock-up](/doc/Start_aid_whireframe_desk.png)

- Mobile

![Mobile mock-up](/doc/Start_aid_whireframe_mobile.png)
- 
**Note that the final design has changed from the original design in the mock-ups. The reason why it has changed. I was trying different layouts while I was experimenting and learning the code and sometimes the new designs looked better than the original ones or was just more responsive. *
 
### Design Ideas

- Navbar
Standard on all the pages there will be a Navbar.  The Navbar will navigate to all sites on the website and  to Home, and have the accounts and search functionality

- The landing page 
Will have a banner with features of the main product on it.   A offer area where there will be the opportunity to go directly to the staraid main product.
A featured product area  where some product will be featured.   And the last will be some comment and review present on the landing page.

- All Product
Will have an overview of all the products available where you can either view or put directly in cart  (for the future there will be favourite )

- Product details
Details of the product that includes photo's , price, stock, Features, specifications, reviews, comment and a link to the cart

- Cart
List of products selected with option to change quantity or empty cart, selection of transport price  and then to proceed to checkout

- Checkout
You can only proceed to checkout if you are signed in  your shipping details will be automatically populated and you only need to do payment fields

- Staraid
Page is a summery of all the features of the product

- Q&A
Page will have in Question and answers 

- New, and Policy, warranty ext. pages 
Are for information

- Contact
- This page will have a contact from

- Footer
The footer will have link to the information pages and a place where you can signup for the newsletter


##### Template used
Used the template Free HTML5 Bootstrap 4 e-Commerce Website Template

## Features

### Existing Features

The website  html pages extend from the base.html page where the navbar and footer is present the content displays on each page by {% block content %} and {% endblock %} tags.:

- Navbar: Every page features the navbar which signals where users can find each page. The navbar hosts the following links: Home, Shop, My Staraid, About, Contact, Search, Cart, Register and Login. The navbar is responsive and the links collapse on smaller screens, and are replaced by a hamburger menu icon.

- Footer: In this section, the user will find additional pages that can be accessed by clicking the links. It also includes the logo payment and shipping term, warranty, and policy,  and a option to subscribe to updates.

### Home App

- Home page

  - The Home page displays a carousel and its main purpose is to get the user attention to the on offer product.  The featured area has 4 main summarized features in.  On offer area highlight the product on offer, where 3 comments are display that refer to the on offer product.
  - The Features product are product that are featured and highlighted 

- Contact page

  - This page features an contact form that will send an email to myself with the customers details.

- Staraid page

  - This is a single page with a lot of textual information about StarAid. It gives information with pictures and videos.
  - 
- FAQs page

  - This page gives the user more information on frequently asked questions.  It has a index with a tag to the text.  There are also a few link that will refer you back to the privacy policy or warranty

- Privacy Policy, Return and warranty, Cookies page, Payment and shipping, Terms and Conditions pages

  - A page like this would be added to any store and website as to European law.

- News page

  - You will find embedded pdf of magazine articles.

### Product App

- Product page

  - This is the page contains a list of all the products in the shop. The page contains cards with a image and price. 

  - With the cards, images are clickable and also the hover eye icon can direct users to the product detail page. There is also an Add to Cart button that adds the item to the customer's cart.  When an item is added to the cart it will not redirect it will show on the navbar that you have and item in the cart.


- Single product Page

  - Once the customer  clicks to the product detail page. They can see a more images of the product and find out specific information about the Features Specification and review and comments.

  - If the customer wants to purchase this product, they can use the Add to Cart button to put the item in their cart. Doing this also redirects the customer to the cart page.
   
  -The customer can also see the available stock

### Search App

- Search navbar

  - On the navbar  users can search products. The can search icon and search overlay or pop up will appear below the navbar.  There they can type their search and press on the search icon

  - Results are displayed and are in the same page as all products page  

### Accounts App

- Login page

  - To proceed to checkout, users must register and login. Regular users can use this page to login as the form will be provide. Users log in by using their username and password. Once logged in, they are directed to the to the checkout page.

  - If a user has forgotten their password, they can use the reset password link below the form.

- Register page

  - Users can register for the website by using the form on this page. New users can register by adding their email address, desired username, password and the password  and personal details must be confirmed. Then the user can press create a account  button.

  - On registering, the new user will be redirected to the Index Page and will see a success message display under the navbar. 

- Update page

  - Users can update their detail except for password and username  on this page. After change they can just click button  update account. 
  - 
- Reset pages

  - Outside the Accounts App, are the reset password pages. You can find these pages in a separate folder in the top level Templates folder in the registration folder.
  
  - Users can find the reset password route when they go through the Reset Form. There is a link to this form at the bottom of the Login page. When the user enters their email address, they receive a reset link to their address.

  - When the reset link is pressed, users are directed to a new form where they can change their password. Once completed, users then see the reset complete form prompting them to login using their new credentials.

### Checkout App

- Checkout page

  - Users must be logged in to proceed to checkout and will be directed to do so if not logged in. If the user logs in, they will move directly to the checkout page.

  - At checkout, there are two forms: the order form and the payment form. Here users will add all relevant information in order to complete checkout the order form will be filled with information from the created profile.

  - On successful completion of payment , users will see a success message at the top of the page and will be directed to the All product page in case they want to purchase more items. If a user is unsuccessful, they will also see a message.

### Shipping App

- Cart page

  - The user can use this app to get the shipping cost that will be added to the total of the cart 

### Cart App

- Cart page

  - This page can be accessed by clicking on the Cart link in the navbar or from All Product or Single Product page. Users will see a brief explanation of the cart and the checkout button.

  - If there are items in the cart, the user will see them display with the total price. The order line items have thumbnail images and the quantities can be adjusted in the cart.

  - Customers also have the option to remove the item from the by changing the quantity to 0..

### News letter App

-  Footer

  - On the footer the customer or prospective customer can subscribe to a newsletter there will be a message got say you are successful and you will receive and email.

### Features Left to Implement

- Blog

  - Where customer can write about their experience and upload photo taken with the product

- Guest shopping

  - For users who want to purchase  but don't want to sign up to the site, this feature would give them a way to do this. This would be in the form of an extra button called 'Guest' that displays when users are prompted to log in.

- Coupon

  - On the cart an place where you can fill in a coupon to get discount
  - 
- Logistics database

  - Have the following data for creating invoice and sending to customer, can login as accountant to see overview of order and invoices, to login as logistics offer see dashboard of stock and open order and have a forecast 
  - 
- Profile page

  - Have a profile page where you can see your order and blogs ext. and load a profile picture.
  
- Cookies popup

  - Put in the cookies popup as i have the policy already.

- Product sorting and show amount

  - At the moment I only have six product but when i get more I will need to add pagination as show amount in the All Product page,  Also I can add the sorting functionality example sorting on price.

## Technologies Used

- Django
- Django Crispy Forms
- Django Storages
- HTML5
- CSS / Bootstrap 4
- SCSS
- JS / JQuery
- Travis
- SQLite3
- PostgreSQL
- Heroku
- Google fonts
- C9 IDE
- Github
- Google Chrome developer
- Pencil
- Diagrams.net
- S3 Amazon Web Services
- Stripe


## Testing

### Continuous Integration - Travis

Continuous Integration - to test code was used with Travis. To see if the built see top of the readme file in GitHub

### Automated tests

#### Account App  the following test has been done and have passed
- Views
    - Test Login
    - Test Register
    - Test Logout
    - Test Update
- Models
    -Test Profile
- Backends
    -Test Case Insensitive Auth
- Forms
    -Test User Login Form
    -Test User Registration Form
    -Test Profile Form
    -Test User Update Forms

#### Cart App  the following test has been done and have passed
- test
    - Test cart
    - Test view
    - Test quantity
    - Test Region
    - Test adjust
    - Test content

#### Checkout App  the following test has been done and have passed
- Views
    - Test redirects
- Models
    -Test labels and quantities
- Forms
    -Test order form and make payment form


#### Product App  the following test has been done and have passed
- Views
    - Test product and single product
- Models
    -Test product and product specification labels

#### Shipping App  the following test has been done and have passed
- Views
    - Test shipping adjust region
- Models
    -Test shipping labels

### Manual testing by feature

- It has been tested with  Chrome Dev Tools 

1. Navbar: Click each link/icon in the navbar to be directed to relevant pages. On mobile or iPad, tap on the links via the hamburger menu icon.
2. On the Index page check that all button link to correct page and that the correct product are hooked to the offer and featured areas
3. Footer checked that all the links are working and that you can subscribe to a newsletter
4. On the All Product page check that you can click on the image or the hover box to go to view or in cart
5. In the Product detail check that you can place a review and have the ability to be approve it in the database by the administrator. 
6. Cart: In the cart, delete an item by making the quantity 0.  Click checkout button to proceed to checkout - if logged in, if not, you'll be asked to log in or register. If successful, you'll be taken directly to the checkout page.
7. Logging in: Fill in the form, you can now proceed to checkout and are logged in.
8. Logging out: Will be visible if logged in already. Click the Logout link in the navbar - redirect to index page and success message displays.
9. Register form: Can be found in the Register link in the navbar then fill out the form with your credentials. You will use those new credentials when logging in.
10. Update Profile: Click in the navbar on update profile only visible when logged in, can update all except for username and password
10. Password Reset: Click the forgot my password link, go to your email inbox and click reset link. Add and confirm new password. Login using new credentials.
11. Search: Type Star to find relevant product. 
12. Contact form: Fill in contact form (by clicking on it in navbar) and check if I receive a mail in my inbox  


## Deployment

### Running the project locally

This project was developed and run locally using a Cloud9.  In Cloud9 a workspace was created where django was installed. Files was added example the README.md file as the first file and then create a .gitignore file in anticipation for the files that i do not want to have visible in Github.

Django i have started a project that will be the folder with the setting file,  And then added extra apps as I went a long.

Crated an env.py file - this file stores all the environment variables needed throughout the project and makes sure important private information isn't pushed to Github. 
Initialise git, add a commit message and then push everything to your online repository. Github  [here](https://github.com/Lemoenskil/E-commerce-webpage-staraid

The project is now visible and accessible locally by using python3 manage.py runserver in your terminal.  Initialise the database and create tables within it by using python3 manage.py makemigrations and then python3 manage.py migrate. 
Create your superuser.  A base.html page as a top level file for the project and when adding new apps (by using python3 manage.py startapp XXX) extend the base.html file to new pages.

### Heroku Deployment

I deployed my project to Heroku at the end of the project.  In Heroku create an app in your account. In the resources tab you can opt for a PostgreSQL database for the project. Selecting this database option pushed my Database URL to the config vars section in the Settings tab in Heroku.

Locally, use pip3 to install dj-database-url to make use of the postgreS database.  In the Settings.py file SQLite database that comes with Django will only be used if  Heroku's PostgreSQL database is not available and when running test. 
I have also install psycopg2-binary==2.8.4 and gunicorn for Heroku deployment.

Add all keys and urls in the env.py file to the config vars section in Heroku. Use python3 manage.py makemigrations and python3 manage.py migrate to create tables in the new database. 

Then create a superuser by using python3 manage.py createsuperuser. Static and Media files are served through Amazon Web Services S3.  pip3 freeze --local > requirements.txt to ensure all dependencies are in place. After this, create the Procfile, which is needed for Heroku to determine what type of app it is.

When the Heroku app url is generated, add it - via an environment variable - to the ALLOWED_HOSTS section in the Settings.py file. When the project is complete,


## Credits

### Photos used:
- All Content comes form Staraid where Pieter Smith have given met the authorization to use for educational proposes


### Content     
- All Content comes form Staraid where Pieter Smith have given met the authorization to use for educational proposes
 

### Work based on other code
- codepen.io for the search bar
- Cindy blog to setup a newsletter https://achiengcindy.com/
- Code institute ecommerce lecturing material code
- Code from the staraid.ai site (polices and FAQs)
- Code from the template that i have used https://demo.themewagon.com/preview/free-html5-bootstrap-4-e-commerce-website-template-eiser

### Acknowledgements

Thanks to my husband for help me test and the many hours of patience
Also, thanks to my mentor Spencer helping to clean my code and the support.
Thanks to stack overflow without it this would not have been possible where I have used a lot of examples.
        
