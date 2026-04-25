### Database Changes

To implement any database changes, you must first drop your public schema. This is to ensure the database matches the development of this branch.
In PostgreSQL's admin tool or the PSQL CLI tool, ensure you are in the correct database that stores the MyDigiRoom user info. Mine for example is named mydigiroom:

![pgAdmin 4 example](/docs/pgadmin4.png)


Run the following commands in PSQL:

``` 
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```
You should have an empty schema such as this example:

![Empty Schema](/docs/schema.png)

Before running these following commands, ensure `mydigiroom/settings.py` is correct otherwise the database will fail to properly migrate.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '[The Database Name]',
        'USER': '[Your Username in PostgreSQL]', 
        'PASSWORD': '[Your Password To Access PostgreSQL]',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

Now, run the following command in the root directory of the project, where `manage.py` is located.

```
python manage.py migrate
```

**You should not have to run `makemigrations`** unless you have changed `users/models.py` or an issue has occured. If you had any superuser account created, you will need to recreate this account.

If everything correctly ran, you should see the following tables:

![Final Schema View](/docs/final.png)

Now, any changes done in `users/models.py` must be migrated by making the migrations, then migrating to the database as Django now manages these database tables.

**DO NOT MAKE MODIFICATIONS OF THE DATABASE THROUGH POSTGRES, YOU MAY BREAK YOUR DATABASE AND NEED TO REDO THESE STEPS.** Please try and avoid making any changes to `users/model.py` unless it is cleared with Diego, as to avoid any desync or further issues. If a change has to be done, please run `python manage.py makemigrations` before migrating the changes to the database, and inform everyone over the changes. When a migration is pushed to the repo, please run `python manage.py migrate` to ensure you are synced. 

If there are any questions, please contact Diego for help troubleshooting.