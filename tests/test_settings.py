DEBUG = True,
SECRET_KEY = 'supersecret'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pgsphere',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    },
}
INSTALLED_APPS = [
    'pgsphere',
    'tests'
]
