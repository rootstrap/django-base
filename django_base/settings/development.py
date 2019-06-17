# Development specific settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_base',
        'USER': 'django_base',
        'PASSWORD': 'django_base',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
