# demo_oye_rickshaw
- API Documentation - https://documenter.getpostman.com/view/5241834/T1DmDJfR?version=latest

# Steps to run the aplication:-
- clone the project - ```git clone https://github.com/Raj160907/demo_oye_rickshaw.git```<br/>
- create and start a virtual environment - ```virtualenv env -p python3```</br>
- Activate virtual environment - ```source env/bin/activate```<br/>
- Install the project dependencies: - 
```pip install -r requirements.txt``` <br/>
- create a postgres db and add the credentials to settings.py - <br/>
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'username',
        'PASSWORD': 'userpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
- connect to your database and run following command -
```sh
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
```
- update database engine -<br/>
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        ...
    }
}
```
```sh
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

# Approach
> - The approach is to create three tables mainly - User, UserLocation and DriverRickshaw.<br/>
> - A foreign key of user goes into the UserLocation Table which specifies the current location of the rider or the driver.<br/>
> - The User table has user_type which specifies of the user is a rider or a driver.<br/>
> - All the user details are stored in the User table.<br/>
> - All the user locations are stored in the UserLocations<br/>
> - Only the lates location of a particular user is set to TRUE and only that is captured during search of drivers.<br/>
> - The third table DriverRickshaw is used to store the vehicle id and the vehicle details of all the drivers so that the vehicle number is sent to the rider, thus easy tracing.<br/>
 
# Assumptions
> - The assumptions made is that the locations of all the drivers will be continuosly update from fronted based on their location coordinates and user_id in the UserLocation table.<br/>
> - One driver will have only vehicle registered to his/her name at a time.<br/>

