# johnlee4.github.io

This follows a tutorial from:
https://realpython.com/build-a-blog-from-scratch-django/
and some templates from  https://www.w3schools.com/w3css/w3css_templates.asp

To use: 
* Fork Repo
* Create conda environment
    * conda create --name git_io --file=environment.yml
* Migrate changes to get sql data
    * python manage.py migrate 
    * python manage.py makemigrations
* create a super user
    * python manage.py createsuperuser
* Run the server
    * python manage.py runserver
    * navigate to 127.0.0.1:8000
* Edit database in admin
    * 127.0.0.1:8000/admin
* Push changes and hope for the best
