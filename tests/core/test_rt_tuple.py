import pytest
from core.rt_tuple import RtTuple

class TestIsVector(object):
    def test_on_tuple_given_findout_is_vector(self):
        vector = RtTuple(0, 0, 0, 1)
        assert vector.is_vector() == True

    def test_on_tuple_given_findout_is_not_vector(self):
        vector = RtTuple(0, 0, 0, 0)
        assert vector.is_vector() == False
    
    def test_on_tuple_given_w_equal_0_5_findout_is_not_vector(self):
        vector = RtTuple(0, 0, 0, 0.5)
        assert vector.is_vector() == False