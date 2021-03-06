import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pgsphere',
    version='0.2',
    packages=['pgsphere', 'pgsphere.migrations'],
    include_package_data=True,
    license='GPL',
    description='A django app that adds pgsphere fields to django models',
    url='https://github.com/LCOGT/django-pgsphere',
    author='Austin Riba',
    author_email='ariba@lcogt.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independant',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'TOPIC :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django',
        'psycopg2'
    ]
)
