#!/usr/bin/env python

import runpy

class TestAssertionError:
    '''
    an_assertion_error.py
    '''

    def test_assertion_error(self):
        '''
        evaluates two equal values
        '''

        runpy.run_path('/home/larson/school work/phase3/python-p3-functions/lib/testing/conftest.py')