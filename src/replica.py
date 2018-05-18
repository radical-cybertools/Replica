#!/bin/env/python

__author__    = "Vivek Balasubramanian"
__email__     = "vivek.balasubramanian@rutgers.edu"
__copyright__ = "Copyright 2017, The RADICAL Project at Rutgers"
__license__   = "MIT"

from kernel.base import Kernel
from exceptions import *
import radical.utils as ru

class Replica(object):


    '''

    '''
    def __init__(self):

        self._uid = ru.generate_id('replica.%(item_counter)04d', ru.ID_CUSTOM)
        self._num_sim_steps = 0
        self._num_ana_steps = 0
        self._kernels = list()

    # --------------------------------------------------------------------------
    # Getters+Setters
    # --------------------------------------------------------------------------
    @property
    def uid(self):
        return self._uid

    @property
    def num_sim_steps(self):
        return self._num_sim_steps

    @property
    def num_ana_steps(self):
        return self._num_ana_steps

    @property
    def wfs(self):
        return self._wfs

    @num_sim_steps.setter
    def num_sim_steps(self, val):
        self._num_sim_steps = val

    @num_ana_steps.setter
    def num_ana_steps(self, val):
        self._num_ana_steps = val

    @wfs.setter
    def wfs(self, val):
        self._wfs = val

    # --------------------------------------------------------------------------
    # Public methods
    # --------------------------------------------------------------------------
    def add_kernels(self, kernel):
        if not isinstance(kernel, list):
            kernel = [kernel]

        for kern in kernel:
            if not isinstance(kern, Kernel):
                raise TypeError(expected_type='Kernel', actual_type=type(kern))

        self._kernels.extend(kernel)

    def get_kernels(self):
        return self._kernels

    def get_kernel_names(self):
        kern_names = list()
        for kern in self._kernels:
            kern_names.append(kern.name)

        return kern_names
    # --------------------------------------------------------------------------
    # Private methods
    # --------------------------------------------------------------------------