# johnlee4.github.io

This follows a tutorial from:
https://realpython.com/build-a-blog-from-scratch-django/
and some templates from  https://www.w3schools.com/w3css/w3css_templates.asp

Export conda environment:
    * $ conda env export --no-builds  > environment.yml 

To use: 
* Fork Repo
* Create conda environment. May need to remove some linux specific dependencies
    * conda env create --file=environment.yml
* install git lfs for large file support in git. May need to do it manually if githooks exists
    * git lfs install 
* Migrate changes to get sql data
    * python manage.py makemigrations
    * python manage.py migrate 
* create a super user
    * python manage.py createsuperuser
* Run the server
    * python manage.py runserver
    * navigate to localhost:8000
* copy the githook and edit
    * open githooks/pre-push and change relavant filepaths
    * cp githooks/pre-push .git/hooks/
* Edit database in admin
    * localhost:8000/admin
* Push changes and hope for the best
