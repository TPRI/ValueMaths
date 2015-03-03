# tests for the Value class

# Imports
from value import Value
from value import IncompatibleUnitsError
from nose.tools import assert_equal, assert_raises, assert_true, assert_false

def test_not_in_unit_defs():
    with assert_raises(KeyError) as exception: Value('furlong')

def test_read_int():
    eight = Value(8)
    assert_equal(eight.coefficient,8)

def test_read_str():
    j = Value('joule')
    assert_equal(j.base_units,{'A': 0, 'kg': 1, 'k': 0, 'm': 2, 'cd': 0, 's': -2, 'mol': 0})

def test_read_dict():
    a = Value({'metre': 2})
    assert_equal(a.base_units,{'A': 0, 'kg': 0, 'k': 0, 'm': 2, 'cd': 0, 's': 0, 'mol': 0})

def test_read_list():
    v = Value({'metre': 1,'second': -1})
    assert_equal(v.base_units,{'A': 0, 'kg': 0, 'k': 0, 'm': 1, 'cd': 0, 's': -1, 'mol': 0})

def test_read_value():
    x = Value('metre')
    m = Value(x)
    assert_equal(m.base_units,{'A': 0, 'kg': 0, 'k': 0, 'm': 1, 'cd': 0, 's': 0, 'mol': 0})

def test_equality_simple():
    m = Value('metre')
    km = Value('kilometre')
    j = Value('joule')
    assert_true(m == m)
    assert_false(m == km)
    assert_false(m == j)

def test_multipication_simple():
    m = Value('metre')
    km = Value('kilometre')
    per_s = Value({'second':-1})
    ten = 10*m
    area = km*ten
    velocity = ten * per_s
    assert_equal(velocity.base_units,{'A': 0, 'kg': 0, 'k': 0, 'm': 1, 'cd': 0, 's': -1, 'mol': 0})
    assert_equal(velocity.coefficient,10)
    assert_equal(area.base_units,{'A': 0, 'kg': 0, 'k': 0, 'm': 2, 'cd': 0, 's': 0, 'mol': 0})
    assert_equal(area.coefficient,10000)

def test_dimension_match():
    joule = Value('joule')
    calorie = Value('calorie')
    hour = Value('hour')
    assert_true(joule.dimension_match(calorie))
    assert_false(joule.dimension_match(hour))

def test_add():
    m = Value('metre')
    km = Value('kilometre')
    s = Value('s')
    dist = m + km
    assert_equal(dist.base_units, {'A': 0, 'kg': 0, 'k': 0, 'm': 1, 'cd': 0, 's': 0, 'mol': 0})
    assert_equal(dist.coefficient, 1001)
    with assert_raises(IncompatibleUnitsError):
        5*m +2*s

def test_to():
    minute = Value('minute')
    seconds = Value('second')
    assert_equal((60*seconds).to('minute'), '1 minute')