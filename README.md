# SoftwareSnakes-10-project-CSCE3444 (MyDigiRoom)

![MyDigiRoom Home Page](/docs/mydigiroom_home.png)

## Project Members

- Lily Hillman
- Bethany de la Torre
- Diego Villela Morua
- Dean Chisolm
- Leaf Sampeck

## Project Idea
"FOR college students WHO are wanting to express their interests and find similar people, THE MyDigiRoom website is a social media platform THAT allows users to decorate a digital room to match their interests and find others with similar interests. UNLIKE other social media (like MySpace), OUR PRODUCT, MyDigiRoom, provides users with a customization interface to decorate their room and allows users to link extra information to the objects in the room that can be accessed by clicking on the objects."

## Trello
[Trello Board](https://trello.com/b/jGi8ajuS/softwaresnakes-10-project-csce3444)

## Scrum Meeting Times
The group will meet during class hours for scrum meetings, alongside wednesdays at 6:30 PM online through Zoom.

Join Zoom Meeting 
https://us05web.zoom.us/j/83044713288?pwd=QFN6uw1LTIY9ZwaBh2ydrrL57aRbPw.1 
Meeting ID: 830 4471 3288 
Passcode: 3igRQJ 

## Prepare to Run Server
To run and develop the proof of concept, install Django using PIP (Python's Package Manager), 
``pip install django psycopg2 pillow`` and allowing it to install the packages.


### Database 
Before you can run the server, you must launch your PostgreSQL server. Modify the settings in `mydigiroom/settings.py` to match the settings of
your PostgreSQL account and database. This tutorial assumes you are running an empty database and schema. If you have items, records, or tables in your database,
please refer to _dbChanges.md_ on how to start the table from scratch.

From the empty database and schema, enter the root directory of the project in a terminal and run the following command: `python manage.py migrate` which
should move the changes required for the backend to function properly into your PostgreSQL database. 

## Testing 

Django has built in Testing support, and a few unit tests were created in `users/tests.py` which test the functionality of the core of the website's backend and database.
This is conducted by creating a test database with the same models and objects as defined in `users/models.py` and simulating a browser client for testing.

To run the test suite, ensure your database settings in `mydigiroom/settings.py` are correct as previously instructed and ensure your database has the proper Django 
migrations when checking the SQL administrative app. 

Then, after all your database settings are correct, and the server can run correctly, you can run the tests by conducting the following command: `python manage.py test`.

## Running the Server

After ensuring all settings are correct, we will launch the server with ` python manage.py runserver ` and the program will run a local server on localhost (127.0.0.1) in debug mode.
You may enter the admin panel using ``127.0.0.1:PORT/admin`` and you may directly interface with the database using the admin panel, but you must make a superuser account using 
`python manage.py createsuperuser` and by following the prompts, you can ignore an email if you wish.

To close the server, simply send an interrupt signal (CTRL-C) to the terminal running the server. This server grants the ability to render the pages
properly and allow user interaction with the database and other aspects of the backend.

![MyDigiRoom Profile Page](/docs/mydigiroom_profile.png)

![MyDigiRoom Explore Page](/docs/mydigiroom_explore.png)


