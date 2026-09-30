# Models from SQL code previously given by Lily. I spent a bit too long on trying to get this sorted out. Oops.

from django.db import models

class Friends(models.Model):
    userid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='userid')
    friendid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'friends'

class Musicdata(models.Model):
    itemid = models.AutoField(primary_key=True)
    musicdata = models.BinaryField()

    class Meta:
        managed = True
        db_table = 'musicdata'


class Objectdata(models.Model):
    itemid = models.AutoField(primary_key=True)
    imagedata = models.BinaryField()

    class Meta:
        managed = True
        db_table = 'objectdata'


class Userinfo(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    email = models.CharField(unique=True, max_length=255)
    college = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=30, default="John Doe")
    profilePicture = models.ImageField(upload_to='pfp', default='pfp/default.png')
    hide_room = models.BooleanField(default=False)
    allow_requests = models.BooleanField(default=True)
    show_profile = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'userinfo'


class FriendRequest(models.Model): # This is a new model to handle friend requests, which was not in the original SQL code but is necessary for the "add_friend" functionality.
    sender = models.ForeignKey(Userinfo, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(Userinfo, on_delete=models.CASCADE, related_name='received_requests')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')


class Userpass(models.Model):
    userid = models.OneToOneField(Userinfo, models.CASCADE, db_column='userid', primary_key=True, null=False)
    password = models.CharField(max_length=127, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'userpass'


class Userroom(models.Model):
    userid = models.OneToOneField(Userinfo, models.CASCADE, db_column='userid', related_name="room", primary_key=True, null=False)
    roomJSON = models.JSONField(default=dict, blank=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'userroom'

