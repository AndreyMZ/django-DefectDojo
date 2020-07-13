#!/usr/bin/env python

from setuptools import setup

setup(
    name='DefectDojo',
    version='1.9.0',
    author='Greg Anderson',
    description="Tool for managing vulnerability engagements",
    install_requires=[
        'defusedxml',
        'Django==2.2.16',
        'django-auditlog==0.4.7',
        'django-custom-field',
        'django-filter==2.4.0',
        'django-imagekit',
        'django-multiselectfield',
        'django-polymorphic==3.0.0',
        'django-crispy-forms',
        'django_extensions',
        'django-rest-swagger==2.1.2',
        'django-slack',
        'django-tagging',
        'django-tastypie-swagger',
        'django-tastypie>=0.12.2',
        'django-rest-swagger==2.1.2',
        'djangorestframework==3.11.1',
        'django-environ==0.4.5',
        'django-axes',
        'gunicorn>=19.1.1',
        'html2text',
        'humanize',
        'jira',
        'lxml',
        'Pillow',
        'psycopg2-binary',
        'pycrypto',
        'python-nmap>=0.3.4',
        'pytz>=2013.9',
        'requests>=2.2.1',
        'sqlalchemy',  # Required by Celery broker transport
        'supervisor',
        'vobject',
        'html2text',
        'django-watson',
        'celery>=4.1.1',
        'kombu>=4.1',
        'sqlalchemy',
        'pdfkit==0.6.1',
        'defusedxml',
        'django-tagging',
        'django-custom-field',
        'django-imagekit',
        'jira',
        'cryptography',
        'lxml',
        'django-multiselectfield',
        'pbr',
        'django-slack',
        'asteval',
        'Markdown==3.3.3',
        'pandas>=0.22.0',
        'django-dbbackup>=3.2.0',
        'whitenoise==4.1.4',
        'django-environ==0.4.5',
        'json-lines==1.2.0'  # requred by yarn audit parser
    ],

    extras_require={'mysql': ['mysqlclient==2.0.1']},

    dependency_links=[
        "https://github.com/grendel513/python-pdfkit/tarball/master#egg=pdfkit-0.5.0"
    ],
    url='https://github.com/DefectDojo/django-DefectDojo'
)
