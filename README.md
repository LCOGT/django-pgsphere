Django-PgSphere
===============

pgsphere is a django app which makes a few fields available
to your models for working with [pgsphere](http://pgsphere.projects.pgfoundry.org/).

Currently the only fields available are

SBoxField
SPointField

SPointField as an `inradius` lookup whiuch makes cone searches possible:

    MyModel.objects.find(location__inradius=((10,20), 1))

where (10,20) is the center of the seach and 1 is the radius, in degrees.


SBoxField as a `contains` method, which makes it possible to find
objects which contain a specific point:

    MyOtherModel.objects.filter(area__contains=(20,10))

Where (20,10) is the point in which you want to find MyOtherModels
that have an area containing that point.

Installation
============

1. Install this package either using pip or setup.py
2. add `pgsphere` to your INSTALLED_APPS
3. Run migrations (insalls the pg_sphere postgresql extension): `./manage.py migrate`
4. Use the fields in your models: `from pgsphere.fields import SPointField, SBoxField`
