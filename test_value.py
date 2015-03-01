# tests for the Value class

# Imports
from value import Value
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

# def test_str_units():
#     m = Value('metre')
#     km = Value('kilometre')
#     assert_equal(j.__str__(),'1 kg  m^2  s^-2 ')