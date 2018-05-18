#!/bin/env/python

__author__    = "Vivek Balasubramanian"
__email__     = "vivek.balasubramanian@rutgers.edu"
__copyright__ = "Copyright 2017, The RADICAL Project at Rutgers"
__license__   = "MIT"

from exceptions import *
import radical.utils as ru

class Engine(object):

    '''

    '''
    def __init__(self):
        self._uid = ru.generate_id('engine', ru.ID_PRIVATE)
        self._wfs = str()