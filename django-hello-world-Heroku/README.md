# Hello, World! Django application with Heroku

Create the docker image and push it to docker hub.

Install Heroku
```Heroku
brew tap heroku/brew && brew install heroku
```
Login to Heroku through terminal
```Login
heroku login
```

Create Heroku app/domain
```Heroku
heroku create <project_name>
```

git init and create remote
```Heroku
heroku git:remote -a <project_name>
```

open app
```Heroku
heroku open
```
