# demo_oye_rickshaw
API Documentation - https://documenter.getpostman.com/view/5241834/T1DmDJfR?version=latest

##Steps to run the aplication:-
1- clone the project - (git clone https://github.com/Raj160907/demo_oye_rickshaw.git)<br/>
2- create and start a virtual environment - (virtualenv env -p python3)</br>
3- Activate virtual environment - (source env/bin/activate)<br/>
4- Install the project dependencies: - (pip install -r requirements.txt)<br/>
5- create a postgres db and add the credentials to settings.py - <br/>
DATABASES = {<br/>
    'default': {<br/>
        'ENGINE': 'django.db.backends.postgresql_psycopg2',<br/>
        'NAME': 'db_name',<br/>
        'USER': 'username',<br/>
        'PASSWORD': 'userpassword',<br/>
        'HOST': 'localhost',<br/>
        'PORT': '',<br/>
    }
}<br/>
6- coonect to your database and run following command -<br/>
CREATE EXTENSION postgis;<br/>
CREATE EXTENSION postgis_topology;<br/>
7- update database engine -<br/>
DATABASES = {<br/>
    'default': {<br/>
        'ENGINE': 'django.contrib.gis.db.backends.postgis',<br/>
        ...
    }<br/>
}<br/>
8- python manage.py makemigrations (run this command)<br/>
9- python manage.py migrate(run this command)<br/>
10-python manage.py runserver (run this finally to use the app).<br/>

###Approach
The approach is to create three tables mainly - User, UserLocation and DriverRickshaw.<br/>
A foreign key of user goes into the UserLocation Table which specifies the current location of the rider or the driver.<br/>
The User table has user_type which specifies of the user is a rider or a driver.<br/>
All the user details are stored in the User table.<br/>
All the user locations are stored in the UserLocations<br/>
Only the lates location of a particular user is set to TRUE and only that is captured during search of drivers.<br/>
The third table DriverRickshaw is used to store the vehicle id and the vehicle details of all the drivers so that the vehicle number is sent to the rider, thus easy tracing.<br/>

####Assumptions
The assumptions made is that the locations of all the drivers will be continuosly update from fronted based on their location coordinates and user_id in the UserLocation table.<br/>
One driver will have only vehicle registered to his/her name at a time.<br/>

