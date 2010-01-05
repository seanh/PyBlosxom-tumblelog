#!/usr/bin/env python

"""tumblelog.py -- a tumblelog plugin for PyBlosxom.

The tumblelog plugin is an EntryParser plugin that lets you write
entries in [YAML](http://yaml.org/) so that you can give each entry
whatever arbitrary data structure you want (i.e. it doesn't always have
to be the title, metadata and body structure that Pyblosxom normally
imposes on all entries). Additionally, the tumblelog plugin causes
Pyblosxom to render entries from each category with a different story
template, instead of the story.yourflavour template entries will be
rendered with a story.yourcategory.yourflavour template, a different
template for each category. The result is a tumblelog.
FIXME: I haven't explained this very well!

   
Tip from willkg:

To make this plugin really versatile I want entries to be written in YAML so they're not restricted to pyblosxom's title, metadata, body entry format, but I wasn't sure how to do it. Will thinks I can just write an entryparser plugin, which takes over parsing of the entry file and so can parse YAML. The cb_entryparser callback would return a dict containing whatever key,value pairs were parsed from the YAML. This dict may or may not have to contain 'title' and 'body' keys, not sure.

The cb_entryparser callback can also set the 'template_name' key in the dict i 
   
"""
import os
import yaml # PyYAML, which ships with this plugin.

def cb_entryparser(entryparsingdict):
    # Register this plugins's `parse` function as the parser function
    # for YAML entries.
    entryparsingdict['yaml'] = parse    
    return entryparsingdict

def parse(filename, request):
    """
    Parse the YAML file.
    """
    entrydata = yaml.load(open(filename,'r').read())    
    return entrydata