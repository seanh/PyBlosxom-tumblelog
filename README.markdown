A Tumblelog Plugin for PyBlosxom
================================

A tumblelog is a kind of blog in which different types of post can have
different structures and templates, and all are rendered in one anarchic
stream. For example, text posts have a title and some body text (like
normal blog posts), link posts have the url being linked to, the link
text, and a comment (like in a linklog), picture posts have an image
file and a caption, a microblog post like on twitter or identica is
just a snippet of text without even a title, etc. You can make up
whatever types of post you want. For examples, check out tumblelog sites
like tumblr.com.

This tumblelog plugin is an entryparser plugin for PyBlosxom that lets
you write entries in the structured markup language [YAML][], and lets
each entry file specify which entry template it will be rendered with.
Your flavour dir will contain lots of entry templates, one for each type
of entry that you use, instead of just one 'story' template per flavour
as is usual with PyBlosxom. Here is an [example of some PyBlosxom posts rendered using this plugin](http://dl.dropbox.com/u/136038/pyblosxom_tumblelog_plugin.html).

[YAML]: http//yaml.org/

This plugin handles `*.yaml` entry files in your data dir. These should
be YAML-formatted text files, that's the only rule, you can create
whatever YAML forms you want. Well, not quite, your YAML must contain a
key, value pair in which the key is `template_name` and the value is the
name of the template to render this entry with. For example, here's the
YAML file for a link post:

    template_name: link
    url: http://crypto.stanford.edu/~blynn/c/index.html
    title: C Craft
    comment: >    
        An opinionated free online book about the craft of C programming,
        looks good.

and here is the corresponding `link` template from my flavour:

    <div class="entry link">
        <div class="date">
            $(date)
        </div>
        <div class="content">
            <a href="$(url)">$(title)</a><br/>
            $(comment)
        </div>
    </div>

as you can see, the template file references the same keys that were
used in the entry file ('date', 'title' and 'comment'). You can make up
whatever keys you want and use them in your posts and templates, but
it's up to you to ensure that your YAML entry files contain the same
keys as used in their corresponding templates. You can
make up whatever template files you want: links, quotes, pictures,
books, and then make entry files for them. For more examples have a look
at the example
[entries](http://github.com/seanh/PyBlosxom-tumblelog/tree/master/entries/)
and
[flavour](http://github.com/seanh/PyBlosxom-tumblelog/tree/master/flavours/html.flav/)
in this repo.

_The tumblelog plugin was written by seanh with help from willkg._
