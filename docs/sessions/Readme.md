# Intro

Sessions are client server relation

--> every user has his own session

Session data is saved on the server in a session storage (s.a. redis)

the client has a cookie with session id

## Settings

Make sure that session entry exists in settings.py for installed_apps and middleware

- f.e. set session age in settings:

```sh
SESSION_COOKIE_AGE = 12000 ## default is 2 weeks
```

## Create method in form in frontend

f.e.

```sh
<form action="/url" method="POST">
```

## Add view

- f.e. with class based view

```sh
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]

        request.session["favorite_review"] = review_id

        return redirect("/reviews/" + review_id)
```


## Which kind of data should be stored in the session

- dont store objects in sessions
- store simple values in the session (strings, numbers, booleans)

## Using session data (read data from the session)

