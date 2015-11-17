from django.db import models
from ast import literal_eval as make_tuple
from django.core.exceptions import ValidationError
import collections
import math


def rad_to_deg(x):
    return x / (math.pi/180)


def deg_to_rad(x):
    return x * (math.pi/180)


def to_tuple(inval):
    try:
        val = make_tuple(inval)
    except (ValueError, SyntaxError):
        raise ValidationError("Invalid input: '{0}'".format(inval))
    if not isinstance(val, collections.Iterable):
        raise ValidationError("Value must be a tuple")
    return val


def parse_spoint(point, to_deg):
    if not isinstance(point, tuple):
        point = to_tuple(point)
    if len(point) != 2:
        raise ValidationError('Point has exactly two values: (ra, dec)')
    if to_deg:
        return tuple(rad_to_deg(i) for i in point)
    else:
        return tuple(deg_to_rad(i) for i in point)


def parse_sbox(points, to_deg):
    if not isinstance(points, tuple):
        points = to_tuple(points)
    if len(points) != 2:
        raise ValidationError('Box has exactly 2 points, SW and NE')
    return tuple(parse_spoint(i, to_deg=to_deg) for i in points)


class SBoxField(models.Field):
    """
    Index this field: CREATE INDEX frames_pstest_location
    ON frames_pstest USING GIST (location);
    """
    def db_type(self, connection):
        return 'sbox'

    def to_python(self, value):
        if value is None:
            return value
        return parse_sbox(value, to_deg=True)

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def get_prep_value(self, value):
        return str(parse_sbox(value, to_deg=False))

    def get_prep_lookup(self, lookup_type, value):
        if lookup_type == 'contains':
            # value will be a point
            return str(parse_spoint(value, to_deg=False))
        else:
            raise TypeError('Lookup type %r not supported' % lookup_type)


@SBoxField.register_lookup
class SboxContains(models.Lookup):
    lookup_name = 'contains'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s ~ spoint %s' % (lhs, rhs), params


class SPointField(models.Field):
    """
    Index this field: CREATE INDEX frames_pstest_location
    ON frames_pstest USING GIST (location);
    """
    description = 'A pgsphere spoint as a tuple (ra, dec) in degrees'

    def db_type(self, connection):
        return 'spoint'

    def to_python(self, value):
        if value is None:
            return value
        return parse_spoint(value, to_deg=True)

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def get_prep_value(self, value):
        return str(parse_spoint(value, to_deg=False))

    def get_prep_lookup(self, lookup_type, value):
        if lookup_type == 'inradius':
            # value will be a tuple ((ra, dec), radius)
            point, radius = value
            return '<{0}, {1}>'.format(
                tuple(deg_to_rad(x) for x in point),
                deg_to_rad(radius)
            )
        else:
            raise TypeError('Lookup type %r not supported.' % lookup_type)


@SPointField.register_lookup
class SPointIn(models.Lookup):
    lookup_name = 'inradius'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s @ scircle %s' % (lhs, rhs), params
