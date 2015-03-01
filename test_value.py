# tests for the Value class

# Imports
from value import Value
from nose.tools import assert_equal, assert_raises, assert_true, assert_false

def test_not_in_unit_defs():
    with assert_raises(KeyError) as exception: Value('furlong')