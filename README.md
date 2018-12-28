#  The ultimate Flicker Client 
In this website, users can bring photos from Flickr by tags. You can also see most recent 20 previous searches at the right sight of the page. If you want to see results of some previous serches, then click! This website uses Flickr API and Django Framework.
Django is a Python web framework. It is also free and open source :) 
## Installation
Before start, if you don't have python3.6 and Django 1.10 or higher versions, you should install python3.6 and Django 1.10.

-The project is on my github repo and available. You can clone it.
```
$git clone https://github.com/ozlemer/hipo.git
```
-After that, come to your project directory to create virtual enviroment:
```
  $virtualenv venv
```
-To activate the virtual enviroment and install the requirements:
```
  $source venv/bin/activate
  $pip install -r requirements.txt
```
-To make migrations to the database:
```
  $python manage.py makemigrations

  $python manage.py migrate
```
-It's almost done. Create a superuser and run the Server.
```
  $python manage.py createsuper

  $python manage.py runserver
```
-Now, you can visit on http://127.0.0.1:8000/ !!! :tada:
