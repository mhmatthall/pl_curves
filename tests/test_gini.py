#!/usr/bin/env python3
'''
unit test for the gini coefficient function
'''
import sys
sys.path.append('..')

from pl_curves.pl import calculate_gini
import pandas as pd
import math


def test_gini_empty():
    '''test calculating a gini coefficient with an empty list
    This will cause some warnings from python
    '''
    gini = calculate_gini(pd.Series([]))
    assert math.isnan(gini) is True


def test_gini_single():
    '''test calculating a gini coefficient with a single item'''
    gini = calculate_gini(pd.Series([1.0]))
    assert gini == 0


def test_gini_four():
    '''test calculating a gini coefficient with four different items'''
    gini = calculate_gini(pd.Series([1.0, 2.0, 3.0, 4.0]))
    assert gini == 0.25


def test_gini_four_even():
    '''test calculating a gini coefficient with four identical items'''
    gini = calculate_gini(pd.Series([1.0, 1.0, 1.0, 1.0]))
    assert gini == 0.0
