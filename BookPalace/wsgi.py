<<<<<<< HEAD
"""
WSGI config for BookPalace project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookPalace.settings')

application = get_wsgi_application()
=======
"""
WSGI config for BookPalace project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookPalace.settings')

application = get_wsgi_application()
>>>>>>> 2c9025f (Initial commit with requirements.txt)
