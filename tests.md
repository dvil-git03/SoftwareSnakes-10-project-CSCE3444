### Unit Testing 

To conduct a unit test suite, ensure your database is updated to any migrations that may have been conducted.

Then, after all your database settings are correct, and the server can run correctly, you can run the tests by conducting the following command: `python manage.py test`

At the moment I have a few tests in `users/tests.py` but feel free to add more to test functionaltiy on the website, and I suggest looking at Django's documentation and my code for an idea on how to write unit tests.

None of the tests I have created *should* fail, but if they do, the script will print out a error or a fail message.

-- Diego