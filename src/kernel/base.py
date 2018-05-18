#!/bin/env/python

__author__    = "Vivek Balasubramanian"
__email__     = "vivek.balasubramanian@rutgers.edu"
__copyright__ = "Copyright 2017, The RADICAL Project at Rutgers"
__license__   = "MIT"

from exceptions import *

class Kernel(object):

    '''
    Kernel.executable = 'Amber'
    Kernel.input_data = [
                            {
                                'mode': 'file',
                                'src': name of source file,
                                'dest': name of destination file,
                                'type': 'copy'
                            },
                            {
                                'mode': 'msg',
                                'src': name of source file,
                                'dest': name of destination file,
                            }
                        ]
    Kernel.output_data = [
                            {
                                'mode': 'file',
                                'src': name of source file,
                                'dest': name of destination file,
                                'type': 'copy'
                            },
                            {
                                'mode': 'msg',
                                'src': name of source file,
                                'dest': name of destination file,
                            }
                        ]
    Kernel.processes = 2
    Kernel.threads_per_proc = 4
    # Other Kernel properties that are executable specific    
    '''

    def __init__(self):

        self._uid = ru.generate_id('kernel.%(item_counter)04d', ru.ID_CUSTOM)
        self._name = str()

        # Data related attributes
        self._input_data = dict()
        self._output_data = dict()

        # Resource related attributes
        self._procs = 1
        self._threads_per_proc = 1
        self._proc_unit = 'cpu'

    # --------------------------------------------------------------------------
    # Getters+Setters
    # --------------------------------------------------------------------------
    @property
    def uid(self):
        return self._uid


    # Data magic
    # -----------------------------------------
    @property
    def input_data(self):
        return self._input_data

    @property
    def output_data(self):
        return self._output_data

    @input_data.setter
    def input_data(self, val):

        if not isinstance(val, dict):
            raise TypeError(expected_type=dict, actual_type=type(val))

        if ['mode','src', 'dest'] not in val.keys():
            raise ValueError(   obj=self._uid, 
                                attribute='input_data', 
                                expected_value = ['mode','src', 'dest'],
                                actual_value = val.keys())

        self._input_data = val

    @output_data.setter
    def output_data(self, val):

        if not isinstance(val, dict):
            raise TypeError(expected_type=dict, actual_type=type(val))

        if ['mode','src', 'dest'] not in val.keys():
            raise ValueError(   obj=self._uid, 
                                attribute='input_data', 
                                expected_value = ['mode','src', 'dest'],
                                actual_value = val.keys())

        self._output_data = val


    # Resource magic
    # -----------------------------------------
    @property
    def procs(self):
        return self._procs

    @property
    def threads_per_proc(self):
        return self._threads_per_proc

    @property
    def proc_unit(self):
        return self._proc_unit

    @procs.setter
    def procs(self, val):
        
        if not isinstance(val, int):
            raise TypeError(expected_type=int, actual_type=type(val))

        self._procs = val

    @threads_per_proc.setter
    def threads_per_proc(self, val):
        
        if not isinstance(val, int):
            raise TypeError(expected_type=int, actual_type=type(val))
            
        self._threads_per_proc = val

    @proc_unit.setter
    def proc_unit(self, val):
        
        if not isinstance(val, str):
            raise TypeError(expected_type=str, actual_type=type(val))
            
        self._proc_unit = val

    # --------------------------------------------------------------------------
    # Public methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Private methods
    # --------------------------------------------------------------------------