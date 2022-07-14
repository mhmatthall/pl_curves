#!/usr/bin/env python3
import sys
sys.path.append('..')

from pl_curves.pl import check_columns
import pandas


def test_check_columns_correct():
    df = pandas.DataFrame([0.4, 0.6])
    assert check_columns(df) is True


def test_check_columns_incorrect():
    df = pandas.DataFrame([0.1, 0.8])
    assert check_columns(df) is False
