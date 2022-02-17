import unittest
import pytest
import math
from carbon_dating import get_age_carbon_14_dating

# Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test against
# this special case.

def test_carbon_dating():
    carbon_14_ratio = 0.35
    if carbon_14_ratio <= 0:
        assert math.isnan(get_age_carbon_14_dating(carbon_14_ratio))
    else:
        assert math.isclose(get_age_carbon_14_dating(carbon_14_ratio) , 8680.34, abs_tol=0.05)