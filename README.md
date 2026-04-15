# SoftwareSnakes-10-project-CSCE3444 (MyDigiRoom)

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

## Run Server
To run and develop the proof of concept, install Django using PIP (Python's Package Manager).
``pip install django ``.

Before you can run the server, you must launch your PostgreSQL server. Modify the settings in `mydigiroom/settings.py` to match the settings of
your PostgreSQL account. Then you must create a migration to move Django's database modifications onto your database, conduct this doing 
` python manage.py makemigrations` , and then `python manage.py migrate` to complete the migration.

Then, before running, ensure your PostgreSQL server is running and your login and settings are correct in `mydigiroom/settings.pu`.
After ensuring all settings are correct, we will launch the server with
`` python manage.py runserver ``.

You may enter the admin panel using ``127.0.0.1:PORT/admin`` and you may directly interface with the database using the admin panel, but
you must make a superuser account using `python manage.py createsuperuser` and by following the prompts, you can ignore an email if you wish.

At the moment, I have migrated the static HTML pages to be Django compliant, and everything should be working as intended. Once the server is running you
will be greeted with the home.html page. To access other websites, since the login logic has yet to be implemented, manually type into the search bar the 
page you'd like to visit.
Examples include:
- /users/myroom
- /users/settings
- /users/friends
- /users/explore
The header should direct you to the correct pages as well.

If you have any questions, please contact Diego. :)


