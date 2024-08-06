## Create folder according to this

```sh
- app-dir
-- templates
--- app-dir
```

## Set template path to overall settings like this

```sh
'DIRS': [
    BASE_DIR / "challenges" / "templates"
],
```

- challenges is the name of the app-dir


or 

add app challenges to the installed apps
```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'challenges',
]
```

## Output variables with interpolation


```sh
return render(
    request, "challenges/challenge.html", {
    "text": challenge_text, 
    "month": month,
})
```

- like in laravel add this

```sh
<h2>{{text}}</h2>
```

## Filter functions in templates

```sh
<h1>{{month | title}} challenge</h1>
```

## For loops

```sh
{% for month  in months %}
    <li> 
        <a href="{% url "month-challenge" month %}"> {{month | title}} </a> 
    </li>
{% endfor %}
```

## If tag

## Core Templates

- template inheritance from templates folder in root folder
- use this for templates that can be used over different apps

## Adding static files

- inside app create a new folder called static -> then create js or css files

f.e. base layout html

```sh
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>
            {% block page_title %}
                My Challenges
            {% endblock  %}
        </title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>
    <body>
        
        {% block content  %}{% endblock  %}
    </body>
</html>
```

## Set up project wide static files

- create new folder /static under the main root dir