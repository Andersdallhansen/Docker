# Hello, World! Django application with Heroku

Create the docker image and push it to docker hub.

Install Heroku
```Heroku
brew tap heroku/brew && brew install heroku
```
Login to Heroku
```Login
heroku login
```

Create Heroku app/domain
```Heroku
heroku create <project_name>
```

create remote
```Heroku
git init
heroku git:remote -a <project_name>
```

Set buildpack
```Heroku
heroku buildpacks:set heroku/python
```
ß
git push to heroku
```Heroku
git push heroku HEAD:master
```

open app
```Heroku
heroku open
```
