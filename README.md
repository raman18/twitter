twitter
Features Covered
  1. Ability to post an update of max length 140 characters
  2. Ability to follow anyone
  3. Ability to view the updates(time sorted in descending, latest update first) of all those the user
  follows. This would be the user's own personalized feed where the user gets to view updates from
  everyone he/she follows in a single stream.
 
The project has been implemented using Django and MySQL.
Configurations for running the app:
  1. Python version 3.8
  2. mysql server 8.0.28.0

After fetching project make virtualenv inside twitter directory
    
    $ pip install virtualenv
    
    $ virtualenv virtualenv_name*

Now to activate virtual env
  
  For Windows
    $ virtualenv_name*\Scripts\activate
  
  For Linux
     source virtualenv_name*/bin/activate

Now we need to run the requirements.txt file, this will provide the required libraries for the app.
  $ pip install -r requirements.txt
  
Now we can create our database using command
  $ python manage.py migrate  
  
After executing requirements.txt file you can start application by
  $ python manage.py runserver

Defualt values are provided but you can change some details, for example you can change database name or instead of MySQL you can use other database.

List of APIs:
  1. Create User.
  2. Post update.
  3. Follow people.
  4. Get followers post.
  5. Login/Logout.
  
Apis specs are provided in json format in postman_collectio.json file.
After creating user we get an access-token, which will be used as Authorization-header for the api calls except login api.


