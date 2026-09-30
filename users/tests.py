from django.test import TestCase
from django.urls import reverse
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Userinfo, Userpass, FriendRequest, Friends


# Create your tests here.

class AccountTests(TestCase):

    # Creating a dummy user account for this test class
    def setUp(self):
        self.testPassword = "@dvanc3dTest1ng!"
        self.testUser = Userinfo.objects.create(username="testing", email="testing@mydigiroom.com", name="Testing Account")
        Userpass.objects.create(userid=self.testUser, password=make_password(self.testPassword))

    # Tests user registraion by creating a new user using these credentials. 
    def test_userRegistration(self):
        # This dictionary contains what a user would normally send in when signing up.
        browserResponse = self.client.post(reverse('authenticate:signup'), {
            'email': 'test2@mydigiroom.com',
            'username': 'testing2',
            'password': "@dvanc3dTest1ng!",
            'name': 'Testing Account #2'
        }) 

        # Checks if the user was created
        user = Userinfo.objects.filter(username='testing').first()
        self.assertIsNotNone(user)

        # Checks if the password was properly hashed and created in the database
        password = Userpass.objects.filter(userid=user).exists()
        self.assertTrue(password)

        # And, we need to ensure they were properly redirected to the login page.
        self.assertEqual(browserResponse.status_code, 302) # 302 == REDIRECTED (HTTP)
    
    # Tests user login using the previously generated account in the setup function.
    def test_userLogin(self):
        user = Userinfo.objects.get(username="testing")

        # Provides the proper username and password from the setup object previously created.
        browserResponse = self.client.post(reverse('authenticate:login'), {
            'username': user.username,
            'password': self.testPassword
        })

        # If we were redirected into our room, AND our session ID matches, then we are good to go! :)
        self.assertRedirects(browserResponse, reverse('users:viewRoom', kwargs={'urlID': user.userid}))
        self.assertEqual(self.client.session.get('userid'), user.userid)

    # If we messed up our credentials, we should be kicked out and told to re-enter our credentials.
    def test_wrongCred(self):
        user = Userinfo.objects.get(username="testing")

        # We are going to messup a password, which should cause an error and deny entry.
        browserResponse = self.client.post(reverse('authenticate:login'), {
            'username': user.username,
            'password': 'VeryWrongPassword!'
        })

        # Because we messed up our credentials, this thing needs to be None, meaning we failed to login and get a session
        self.assertIsNone(self.client.session.get('userid'))

        self.assertEqual(browserResponse.status_code, 200) # Basically, the page should refresh, meaning we messed up our login.

    # Tests if we can make a duplicate user, using the previously supplied user and a "new" user (hehe)
    def test_duplicateUsers(self):
        user = Userinfo.objects.get(username="testing")

        with transaction.atomic(): # Since this DB is atomic, we must have the ability to rollback our changes in case a query fails. Which, in this case, it will.
            browserResponse = self.client.post(reverse('authenticate:signup'), {
                'email': 'duplicate@mydigiroom.com',
                'username': user.username,
                'password': "thisshouldfail",
                'name': 'The REAL Test Account'
            }) 

        userCount = Userinfo.objects.filter(username=user.username).count() # Because it failed, we should still have only one account.
        self.assertEqual(userCount, 1)

    # If we try to access, say the explore or friends page without a valid session, then we must be redirected back to "authenticate/login" correctly.
    def test_properSessionBlocking(self):
        # Properly logging out.
        self.client.logout()

        browserResponse = self.client.get(reverse('users:explore'))

        self.assertEqual(browserResponse.status_code, 302) # Properly redirected
        self.assertIn('authenticate/login', browserResponse.url) # and in the proper login page, meaning you are not signed in.


class RoomTests(TestCase):

    # Creating two dummy user accounts for this test class
    def setUp(self):
        self.testPassword = "@dvanc3dTest1ng!"
        self.testPassword2 = "Sudd3n1yTest1ng!"
        self.testUser = Userinfo.objects.create(username="testing", email="testing@mydigiroom.com", name="Testing Account")
        self.testUser2 = Userinfo.objects.create(username="testing2", email="testing2@mydigiroom.com", name="Testing Account #2")
        Userpass.objects.create(userid=self.testUser, password=make_password(self.testPassword))
        Userpass.objects.create(userid=self.testUser2, password=make_password(self.testPassword2))
    
    # Visiting our own room, to ensure we can test accessing our own room
    def test_vistingSelfRoom(self):
        # Logging into our account
        user = Userinfo.objects.get(username="testing")

        browserResponse = self.client.post(reverse('authenticate:login'), {
            'username': user.username,
            'password': self.testPassword
        })

        # Accessing the url 'users/room/{user.userid} which should be our own room.
        browserResponse = self.client.get(reverse('users:viewRoom', kwargs={'urlID': user.userid}))
        
        self.assertEqual(browserResponse.status_code, 200) # OK (HTTP)
        self.assertEqual(browserResponse.context['targetedUser'].username, 'testing') # Our targeted user is our own, meaning it properly recognized it is our room.

    # Entering another users room, by giving their user ID as an arguemnt, and seeing if we are properly directed to their room.
    def test_visitingOtherRoom(self):
        user = Userinfo.objects.get(username="testing")
        visting = Userinfo.objects.get(username="testing2") # Our second user we will be testing by visiting their room.

        browserResponse = self.client.post(reverse('authenticate:login'), {
            'username': user.username,
            'password': self.testPassword
        })

        # Accessing the url 'users/room/{user.userid} which should be testing2's room.
        browserResponse = self.client.get(reverse('users:viewRoom', kwargs={'urlID': visting.userid}))  

        self.assertEqual(browserResponse.status_code, 200)
        self.assertEqual(browserResponse.context['targetedUser'].username, 'testing2') # Our targeted user is testing2, meaning it properly recognized it is testing2's room.
    

    # Visiting a room that does not exist, we set a fake urlID to test this.
    def test_vistingFakeRoom(self):
        user = Userinfo.objects.get(username="testing")

        browserResponse = self.client.post(reverse('authenticate:login'), {
            'username': user.username,
            'password': self.testPassword
        })

        browserResponse = self.client.get(reverse('users:viewRoom', kwargs={'urlID': 99}))

        self.assertEqual(browserResponse.status_code, 404) # As specified by the view, this should be a simple 404 (Not Found) error.



class ProfileSettingsTests(TestCase):
    # Creating a dummy user account for this test class
    def setUp(self):
        self.testPassword = "@dvanc3dTest1ng!"
        self.testUser = Userinfo.objects.create(username="testing", email="testing@mydigiroom.com", name="Testing Account")
        Userpass.objects.create(userid=self.testUser, password=make_password(self.testPassword))
    
    # Can we access the profile page logged into our test account?
    def test_accessProfile(self):
        # Logging in
        user = Userinfo.objects.get(username="testing")

        browserResponse = self.client.post(reverse('authenticate:login'), {
            'username': user.username,
            'password': self.testPassword
        })

        browserResponse = self.client.get(reverse('users:profile')) 
        self.assertEqual(browserResponse.status_code, 200) # 200 (OK) means we are in


    def test_changeProfile(self):
        user = Userinfo.objects.get(username="testing")

        browserResponse = self.client.post(reverse('authenticate:login'), {
            'username': user.username,
            'password': self.testPassword
        })

        veryRealImage = SimpleUploadedFile("test.png", b"file_content", content_type="image/png") # Creating a dummy image to test uploading pfps

        # Going into the profile page
        self.client.get(reverse('users:profile'))
        

        with transaction.atomic(): 
            browserResponse = self.client.post(reverse('users:updateProfile'), {
                'email': "newemail@mydigiroom.com",
                'name': "New Testing",
                'username': 'newtesting',
                'password': 'Newp@ssw0rd',
                'college': 'University of Testing',
                'password': '',
                'profilePic': veryRealImage
            },
            format="multipart")

        self.testUser.refresh_from_db() # Ensuring we are getting the latest cahnges from our database


        newUser = Userinfo.objects.filter(username='newtesting', email="newemail@mydigiroom.com", college='University of Testing').exists()
        self.assertEqual(browserResponse.status_code, 302) # This means our POST was successful and we successfully submitted this new user information.
        self.assertIsNotNone(newUser) # This new user still exists!

        self.assertEqual(self.testUser.username, 'newtesting') # And our session is now using our new username
