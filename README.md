# E-commerce-website-Staraid

This web application has been designed and built for the requirements of the "Data Centric Development" project of the Code Institute Full-Stack Software Development course.  It is intended to be a personal planning tool for vegetable and fruit  gardeners in North Brabant, The Netherlands, where I live and have my own vegetable and Fruit garden, and I hope to continue to develop it going forward.

Offering this tool to the local hobby gardeners i hope the get the best input and tips to grow the perfect vegetable.  With the experience and  I hope to get the correct species for plant that if fit for my region and also the best planting methods for a optimum yield.

The project can be viewed [](herokuapp.com/)

## Specification / Design

Setting up  a database of vegetables that can be grown in North Brabant, which can be changed and new contributions can be made for local vegetable gardeners.

For each vegetable/ Fruit grown, the database will store its common names, crop group (leafy, fruit. root, bulb etc.), information (e.g.  soil, feeding position etc..), notes, and photographs.   Calendar will be available that will show time to sow indoors, time to sow outdoors, and time to harvest.

The user can logging to have access to the  all vegetables in the database, with buttons to view, edit or delete them.  Without logging in the user will have the functionality to browse or search in the database.    The calendar will be showed in table format which will make it easier for planning purposes. 

Clicking "View" for a vegetable will cause a detailed view to be displayed. with a photograph.   User with accounts  will be able to upload photographs for a new entry, to add to an existing entry or replace an existing image.

User will be allowed to register just by logging in with a username.  Registered users will be automatically approved as editors and as such will have full CRUD permissions.   Unregistered users will not be able to update or delete records.
The vegetables will be stored as documents in a non-relational MongoDB database.   The app will be hosted with Heroku.
 
## UX
 
#### Build Data Centric Website for Garden planning

The E-commerce-website-Staraid has the following requirements

Their primary target audiences are herb, vegetable and fruit gardeners or prospective gardeners
The website need to include the following 
- Database with plants 
- Ability to add new plant records 
- The ability to change existing records 
- The ability to delete records
- View a single records
- Search for plant records
- View the plant calendar
- Browse the website with out signing in 
- Only user signed in can update, create and delete records

I need the following for the website
- logo/ Name
- Data Base for the plant records (source of information)
- Picture for the landing page

#### User stories
- As a user, I want to know more about the plants and when to grow them.
- As a user, I'd like to see clean, well presented website that is easy to navigate
- As a user, I'd like to see a variety different plants
- As a user, I’d like for the website to be made so that it will work and adapt to all manner of devices (responsive design) 
- As a user, I want to read on tips and the best way to grow the plant.
- As a user, I want add new plants to the database and have the ability to change or delete it when is have new tips.  
- As a user, I want to have a overview of the plant calendar for the plant in my data base
- As a user, I'd like to see some text to explain what is can expect on the website (instructions) 
- As a user, I'd like to see engaging use of colour making the website pleasant to look at and keeping the user interested 
- As a user, I'd want to navigate easily and always have the ability to return to the home page
- As a user, I want to login to be able to make changes in the database
- As a user, I want to browse through the available plant records

### Project Purpose

I am creating a website aimed towards helping current and prospective gardeners getting an overview of plants (vegetable and fruit) that was planted successfully in my region. 
The website will use MongoDB database, flask and CSS to give the data through to the frontend.    
The information that is available for the plant will help you to plant it in the right manner which will include information on soil, pests, position, harvest and feeding.
When a registered user logon he/she will have the ability to change, add or delete the current records
A not registered user will be able to browse search and view the data on plants.  
Included is an overview of the plant calendar where the user can have an quick overview when to plant what.   

### Scope of website
- A Responsive website that is connected with a unstructured database
- A page to give an overview to browse, search the plants
- A form to change and create a plant records
- A page with a plant calendar table
- Logon ability for a user

### Website Structure

### Mock-up’s

In the links below you can see the mock-up’s that I drew using the mock-up tool “Balsamiq”:
![Desk top mock-up](/static/images/mockup_garden_planner.jpg)
![Mobile mock-up](/static/images/mockup_garden_planner_mobile.jpg)
- 
**Note that the final design has changed from the original design in the mock-ups. The reason why it has changed. I was trying different layouts while I was experimenting and learning the code and sometimes the new designs looked better than the original ones or was just more responsive. *
 
### Design Ideas

- Navbar and Footer
Standard on all the pages there will be a Navbar and footer.  The Navbar will navigate to Home, add Plant, Plant Calendar and Registered

- The landing page 
Wil have a maximum of 6 cards displayed with a picture and a plant name. A Jumbotron with a search bar will be shown on top 

- Single plant view
Will have a picture, a plant table and the information on the plant.  A floating button will be available when you are loged in to change or delete the record.

- Add Plant/Crops
page will be a form where you can create the date.  The table will be updated using a checkbox.  and there will be a submit button.

- Edit, Delete and view Plant/Crops
page will be a form where you can update the date (change or delete.  The table will be updated using a checkbox.  button for delete and change with a modal.

- Search result page
This page will sow the result of the search of the name crops or nots.

- Plant Calendar
From the Navbar you can navigate here.  A table will be on this page

- Register page
Page will have a form and a submit button

- login page
Form with a warning and a submit button


##### Font
Google fount Roboto is used

##### Colour Scheme
Green Orange and White Scheme with a purple Jumbotron

## Features

### Existing Features

- All pages feature a navigation bar at the top, see useful links, or login / logout. 
- Upon viewing the page  the navbar will give you the option to login/or out, go to plant calendar, home , register or add plant
- On the landing page maximum of 6 cards will be displayed if you want to browse you can use the page navigation on the bottom.  You can also click on the card that will take you to the plant overview page.
- On the top of the landing page below the navbar you will find a jumbotron with a search bar, which will allow you to search on the name, crop group or notes.
- On the view page there will be a floating button on which you can either delete or edit the records.  When editing it will redirect you to a form, when deleting it will redirect you to a modal
- From the navigation bar you can be directed to  the add record form
- Both add record and edit record form have a Table with checkbox to select the plant calendar.
- The search bar in the Jumbotron will give you the option to search the data base and redirect you to a page with search results
- In the navbar you are redirected to the register page where you can create a user using a form.
- The option to login is also on the landing page, which will redirect you to a form to login
- In the responsive view for mobile with a side nav bar and the basic sizing
- The creation of an account to edit add and delete records.
- Option on the login screen to register. 

### Features Left to Implement

- Want to make different data object with set fields that you can choose from example pest type, soil types.
- Want to make it more sociable add a blog where user can discuss different topics regards to gardening
- Proper, secure user registration and authorisation.
- Augmenting the styling and visual effect and improved content.
- I have lose properties like soil, position, pest that i can use later to put into dashboard to make the data more visual
- A option to create your own account select your plants and get your own calendar


## Technologies Used

- Python
- HTML5
- CSS / Bootstrap 4
- CSS / Materialize
- JS / JQuery
- Mongo
- Flask
- Heroku
- Google fonts
- C9 IDE
- Google Chrome developer


## Testing

The app has been manually tested extensively throughout the development process, and when bugs have been found they where fixed or a workaround was implemented.

The plant_records page and is tested that they loads the data, the pagination work, and the links are working correctly.

The registration page are tested, for mismatched passwords, duplicate user names, as well as successful registration that is show when the username is on the navbar.

The login page is tested as all scenarios for delete, change and created operations required a logged in user. 

The add_plant page is tested by checking that a plant is entered on submit, the page redirects and the new plant is seen on the plant record page.

The plant_records page search functionality  is tested by searching for plant on the  page, getting its id number and going to that search_results page.  

The update_plant page is tested by going to a logged in users view_plant and then via the floating button edit to update_plant page and changing some data and committing it. This the redirects the user to the plant_records page and check that the information has changed on that plant record. 
  
The delete functionality is tested by going via view_plant to delete where you get modal as a warning and deleting it, then checking the redirect has happened and that the plant does not appear on the plant_records page.

The list plant page is teste by going via the navbar to the page and check that the data has loaded.

The logout functionality was tested via the navbar a logged in user can logout I have test that as then the name was not visible and the option to sign in was on the navbar and the footer.

As the site is built with a responsive design it works for mobiles it has been checked  on iPhones 6 to X, Samsung Galaxys, iPads (mini to pro), Google's Pixel 2 and 3.

It has been tested with  Chrome Dev Tools and on my Android phone. 

Test CSS with css-validator

Test HTML with validator.w3

## Deployment

The app is deployed to Heroku and can be accessed at [].

Version control is implemented in git, by pushing the project directory to Github at [https://github.com/Lemoenskil/Milestone_project_3_Garden_planner], as well as pushing to Heroku.   
I have largely used  with detailed commit messages, to trace back changes, 
       
The database is hosted at MongoDB Atlas.
The details of the database connection are found inside the requirements.txt - it uses the os class environ method to point Heroku to its own config variable (MONGOBD_URI) in order to keep the production database connection string secret.
A Procfile is used to help Heroku to identifies them commands that are run by the application's dynos and how to run pieces of the app including the starting point app.py

## Credits

### Photos used:
Pictures used, Two gardener steampunk toys with a strawberry bush grown in a flower pot, Purchase code: 6420eb4f-b12f-48f9-842e-71d16f4bb7a5
Link to plant pictures are random an my be protected but it was tried to avoided

### Content     

 

### Work based on other code
Code from all the frameworks as Materialize, Bootstrap, Flask Forms  and Stackoverflow  that i have used, And the code from the Task Manager from the code institute                               

### Acknowledgements

Thanks to my husband for help me test and the many hours of patience
Also, thanks to my mentor Spencer helping to clean my code and introducing me to Flask forms to sort out the user login issues.
Thanks to stack overflow without it this would not have been possible where I have used a lot of examples.
        