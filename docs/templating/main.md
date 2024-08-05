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
