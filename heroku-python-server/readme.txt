## Running Locally (within this directory)

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

$ heroku local:run python manage.py migrate
$ python manage.py collectstatic
$ heroku local

App should now be running on [localhost:5000](http://localhost:5000/).


## Deploying to Heroku

$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
