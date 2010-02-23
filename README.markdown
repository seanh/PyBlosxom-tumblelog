A Tumblelog Plugin for PyBlosxom
================================

This is an entryparser plugin that handles several types of entry file:
`*.text`, `*.link`, `*.quote`, `*.picture`, `*.video`. A file format is defined
for each new entry type, these are simple and inspired by PyBlosxom's default
file format. See `entries/` for examples of the tumblelog file formats in use.

Instead of using the `story` template each type of entry is rendered
with its own template: `text`, `link`, `quote`, `picture`, `video`. See
`flavours/` for example flavour templates.

Markdown syntax is supported (e.g. in the bodies of text and link
entries, in quotes, in picture captions, etc.) if python-markdown is
installed on your system (or the python-markdown source is in your
plugins directory).

You could easily add a new entry type by adding a new
`parse_my_entry_type` function in `plugins/tumblelog.py` following the
example of the `parse_*` functions that are already there. You would
need to add a template for the new entry type to each of your flavours
too.
