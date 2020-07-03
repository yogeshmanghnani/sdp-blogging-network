# The Blogging Network
This is a project I am developing as a small side project.
It is written in Python>=3.7 and uses Django 2.2

# Installing 
Before you test this project you need to install it's dependencies
The dependencies of this project are in the requirements.txt
Make sure you are in a Python>=3.7 virtual environment.

``` 
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

By default this will use db.sqlite3 as the database.
You can overide this by creating local_settings.py

# TODO
Write a good README

## vim settings
### python
```
set ts=4
set sw=4
set sts=4
set noexpandtab
set list
set listchars=tab:>-
```
### htmldjango
```
set noet
set ts=2
set sw=2
set sts=2
set nolist
set listchars=""
```
