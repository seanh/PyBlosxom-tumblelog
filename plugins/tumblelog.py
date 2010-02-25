#!/usr/bin/env python
"""tumblelog.py -- a tumblelog plugin for PyBlosxom.

TODO

*   Use pyblosxom's callback system to support tumblelog entry parsers.
    I think the markdown processing could be extracted into a separate
    plugin using the cb_preformat or cb_postformat callbacks. This
    plugin may need to call those callbacks.

*   Improve the HTML templates, make sure they're valid HTML and CSS and use
    the relevant HTML features.

*   Write templates for each tumblelog entry type for the rest of the default
    flavours: RSS, RSS 2, Atom, Error.

*   Support optional click-through links in picture entries like tumblr does.

*   Write more entry types: chat? audio? tweet? code snippet?

*   Make all of the parse functions more robust to IOErrors and invalid
    entry files. Instead of failing silently or crashing (and bringing down
    pyblosxom) revert to an error template.

*   Use YAML-style 'key: value' syntax for metadata instead of pyblosxom's '#key value',
    and allow multi-line metadata entries by indentation.

*   Get rid of some code duplication.

"""
import os

try:
    import markdown 
    md = markdown.Markdown(
        output_format = 'html4',
        # codehilite requires python-pygments
        extensions = ['extra','codehilite'])
except ImportError:
    md = None

def convert(text):
    if md:
        try:
            html = md.convert(text)
            md.reset()
            return html
        except markdown.MarkdownException:
            # FIXME: Log the error with pyblosxom's logger instance.
            pass
    return text

def cb_entryparser(entryparsingdict):
    """
    Register this plugin's `parse_*` functions as the parser functions
    for their corresponding entry filename extensions.
        
    """
    entryparsingdict['text'] = parse_text
    entryparsingdict['link'] = parse_link
    entryparsingdict['picture'] = parse_picture
    entryparsingdict['quote'] = parse_quote
    entryparsingdict['video'] = parse_video
    return entryparsingdict


def parse_text(filename, request):
    
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        return {"title": "", "body": ""}
    
    entry_data = {'template_name':'text'}
    
    title = lines.pop(0).strip()
    entry_data['title'] = title
    
    while lines and lines[0].startswith("#"):
        meta = lines.pop(0)
        meta = meta[1:].strip()     # remove the hash
        meta = meta.split(" ", 1)
        entry_data[meta[0].strip()] = meta[1].strip()

    body = ''.join(lines)
    entry_data['body'] = convert(body)

    return entry_data

def parse_link(filename, request):
    
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        return {"title": "", "body": ""}
    
    entry_data = {'template_name':'link'}
    
    title = lines.pop(0).strip()
    entry_data['title'] = title

    href = lines.pop(0).strip()
    entry_data['href'] = href
    
    while lines and lines[0].startswith("#"):
        meta = lines.pop(0)
        meta = meta[1:].strip()     # remove the hash
        meta = meta.split(" ", 1)
        entry_data[meta[0].strip()] = meta[1].strip()

    body = ''.join(lines)
    entry_data['body'] = convert(body)

    return entry_data

def parse_picture(filename, request):
    
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        return {"title": "", "body": ""}
    
    entry_data = {'template_name':'picture'}
    
    title = lines.pop(0).strip()
    entry_data['title'] = title

    src = lines.pop(0).strip()
    entry_data['src'] = src
    
    while lines and lines[0].startswith("#"):
        meta = lines.pop(0)
        meta = meta[1:].strip()     # remove the hash
        meta = meta.split(" ", 1)
        entry_data[meta[0].strip()] = meta[1].strip()

    body = ''.join(lines)
    entry_data['body'] = convert(body)

    return entry_data

def parse_quote(filename, request):
    
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        return {"title": "", "body": ""}
    
    entry_data = {'template_name':'quote'}
    
    quote = ''
    while lines and lines[0].startswith(">"):
        line = lines.pop(0)[1:]
        quote = quote + line
    entry_data['quote'] = convert(quote)

    cite = '<cite>' + lines.pop(0).strip() + '</cite>'
    entry_data['cite'] = convert(cite)

    while lines and lines[0].startswith("#"):
        meta = lines.pop(0)
        meta = meta[1:].strip()     # remove the hash
        meta = meta.split(" ", 1)
        entry_data[meta[0].strip()] = meta[1].strip()

    body = ''.join(lines)
    entry_data['body'] = convert(body)

    return entry_data

def parse_video(filename, request):
    
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        return {"title": "", "body": ""}
    
    entry_data = {'template_name':'video'}
    
    embed = lines.pop(0).strip()
    entry_data['embed'] = embed

    while lines and lines[0].startswith("#"):
        meta = lines.pop(0)
        meta = meta[1:].strip()     # remove the hash
        meta = meta.split(" ", 1)
        entry_data[meta[0].strip()] = meta[1].strip()

    body = ''.join(lines)
    entry_data['body'] = convert(body)

    return entry_data
