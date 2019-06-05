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
