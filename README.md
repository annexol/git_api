# Test task API

Viewing data about user repositories

### Installation process

<pre>
mkdir test_task_api && cd test_task_api && \
git clone https://github.com/annexol/git_api.git
</pre>

### Guideline

After opening the project(rocket_api) you need to run the commands in the terminal

<pre>
pip install -r requirements.txt
</pre>
### Guideline

In the file .../rocket_api/git_settings.py you must set parameters for YOUR database

<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'task',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',

    }
}
</pre>


...after to run the command in the terminal...

<pre>
manage.py make migrations
manage.py make migrate
</pre>

Creating speruser

<pre>
manage.py createsuperuser
</pre>


####You can use https://github.com/annexol/scrapy_part1
to add data to the data base, but before that change the data_base.py file to save the data into PostgreSQL

Run server

<pre>
manage.py runserver
</pre>

due to the implementation of API access by Token
you have to log in

<pre>
.../admin
</pre>


After you can use follow urls to view data

<pre>
.../api/users
.../api/repositories 
.../api/user/<slug:name>
.../api/common_static 
.../api/detail/<slug:name> 
</pre>


to save data about users repositories

<pre>
.../swagger
</pre>
