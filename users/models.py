# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Friends(models.Model):
    userid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='userid')
    friendid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'friends'


class Hashpass(models.Model):
    userid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='userid')
    pwordhash = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hashpass'


class Musicdata(models.Model):
    itemid = models.AutoField(primary_key=True)
    musicdata = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'musicdata'


class Objectdata(models.Model):
    itemid = models.AutoField(primary_key=True)
    imagedata = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'objectdata'


class Userinfo(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    email = models.CharField(unique=True, max_length=255)
    college = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'


class Userpass(models.Model):
    userid = models.ForeignKey(Userinfo, models.DO_NOTHING, db_column='userid')
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userpass'


class Userroom(models.Model):
    userid = models.ForeignKey(Userinfo, models.DO_NOTHING, db_column='userid')
    backgroundid = models.ForeignKey(Objectdata, models.DO_NOTHING, db_column='backgroundid')
    roomitem1id = models.IntegerField(blank=True, null=True)
    roomitem2id = models.IntegerField(blank=True, null=True)
    roomitem3id = models.IntegerField(blank=True, null=True)
    roomitem4id = models.IntegerField(blank=True, null=True)
    roomitem5id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userroom'


class UsersFriends(models.Model):
    id = models.BigAutoField(primary_key=True)
    friendid = models.IntegerField(db_column='friendID')  # Field name made lowercase.
    userid = models.ForeignKey('UsersUserinfo', models.DO_NOTHING, db_column='userID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_friends'


class UsersUserinfo(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    college = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users_userinfo'


class UsersUserroom(models.Model):
    id = models.BigAutoField(primary_key=True)
    backgroundid = models.IntegerField(db_column='backgroundID')  # Field name made lowercase.
    roomitem1id = models.IntegerField(db_column='roomItem1ID')  # Field name made lowercase.
    roomitem2id = models.IntegerField(db_column='roomItem2ID')  # Field name made lowercase.
    roomitem3id = models.IntegerField(db_column='roomItem3ID')  # Field name made lowercase.
    roomitem4id = models.IntegerField(db_column='roomItem4ID')  # Field name made lowercase.
    roomitem5id = models.IntegerField(db_column='roomItem5ID')  # Field name made lowercase.
    userid = models.ForeignKey(UsersUserinfo, models.DO_NOTHING, db_column='userID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_userroom'
