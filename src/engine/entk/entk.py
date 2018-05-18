#!/bin/env/python

__author__    = "Vivek Balasubramanian"
__email__     = "vivek.balasubramanian@rutgers.edu"
__copyright__ = "Copyright 2017, The RADICAL Project at Rutgers"
__license__   = "MIT"

from ..base import Engine
from exceptions import *
import radical.utils as ru

class EnTK_Engine(Engine):

    def __init__(self):

        super(EnTK_Engine, self).__init__()

        self._wfs = 'EnTK'
