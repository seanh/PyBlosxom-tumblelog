#!/usr/bin/env python
"""tumblelog.py -- a tumblelog plugin for PyBlosxom.

"""
import os
import yaml # PyYAML, which ships with this plugin.

def cb_entryparser(entryparsingdict):
    """
    Register this plugin's `parse` function as the parser function
    for YAML entries.
        
    """
    entryparsingdict['yaml'] = parse    
    return entryparsingdict

def parse(filename, request):
    """
    Parse the YAML file.
    
    """
    entrydata = yaml.load(open(filename,'r').read())    
    return entrydata
