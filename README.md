# Making a Django Portfolio :shit: :shit: :shit:

### 1. Create the Django project
In the folder that you wish the create your portfolio execute:
```shell
django-admin startproject portfolio
```
This will create a new directory called `portfolio` which has a subdirectory
with the same name. It is suggested that you rename the parent directory
to something to something such as `portfolio-project` to avoid ambiguity.


### 2. Test the Server
With `manage.py` in your working directory, run the following command
and navigate to the url that it outputs:

```shell
python3 manage.py runserver
```

### 3. Create a Django App
Individual pieces in a Django project are called apps and they can be
initiated with the following:

```shell
django-admin startapp [appname]
```


It is common that apps have a plural name such as `jobs` which is what we will
use to develop our portfolio.


### 4. Update Files to Run Server
First navigate to the project directory created in the sub project directory
and open `urls.py`. Under the import statements add 
```python3
import jobs.views
```

and in the url patterns list add
```python3
path('name', jobs.views.name, name='name'),
```

### 5. Database

Model - python class that can be saved into a database
Inside of jobs folder open models.py
```python3
from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')

    summary = models.CharField(max_length=200)
```

Postgresql
- click server settings
- make sure port is 5432
- check automatically start server
- initialize
- click postgres icon
- \password postgres
- enter password
- CREATE DATABASE portfoliodb;
- navigate to settings.py and update DATABASES
- change sqlite3 to postgresql
- change NAME: 'portfoliodb'
- add 'USER': 'postgres',
'PASSWORD': 'ram22899'
'HOST': 'localhost'
'PORT': '5432'

### 6. Addressing Migration Errors
Migration - way to set up database for a project. 
- navigate to models.py
- run makemigrations anytime you make a new model or update a model
`python3 manage.py makemigrations`
`python3 manage.py migrate`
this means that we are able to add things into the database now

### 7. Adding to Database with Admin
navigate to serverpage/admin
create a terminal for admin login
`python3 manage.py createsuperuser`
navigate to `admin.py` in `portfolio-project/jobs`
`from .models import Job`
`admin.site.register(Job)`

### 8. Adding a Job
navigate to admin, click on add job
upload image and summary
uploading an image creates a new `images` folder in the project directory

### 9. Moving Database Items to Homepage
navigate to `views.py`

```python3
# in views.py add these

from .models import Jobs

def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
```

now everything should show up on the homepage


### 10. Adding Bootstrap
copy source code from album bootstap example page
and paste into your homepage html file
edit each section along with video


### 11. Adding Static Images in Django
Inside jobs folder make a new folder called static

