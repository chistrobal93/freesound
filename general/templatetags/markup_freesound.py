"""
This was copied directl from django, but a small hack was added to allow different configuration of
markdown. It uses MARKDOWN_FILTER_SETTINGS from settings.py
"""

import markdown as markdown_package
import re

from django import template
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe

register = template.Library()


def markdown(value, arg=''):
    """
    Runs Markdown over a given value, optionally using various
    extensions python-markdown supports.

    Syntax::

        {{ value|markdown:"extension1_name,extension2_name..." }}

    To enable safe mode, which strips raw HTML and only returns HTML
    generated by actual Markdown syntax, pass "safe" as the first
    extension in the list.
    """

    extensions = [e for e in arg.split(",") if e]
    extension_configs = {
        'wikilinks': [('base_url', '/help/'), ('end_url', '/'), ('html_class', 'wikilink')]
    }

    md = markdown_package.Markdown(extensions=extensions, extension_configs=extension_configs)
    html_contents = md.convert(force_str(value))

    # Markdown TOC extension adds target ids to the header tags (e.g. <h2 id="xxx">), but this does not work well
    # in BW frontend because we need to offset the targets to compensate for the fixed header height, and the technique
    # we use needs the target to be set as an anchor (e.g. <a name="xxx"/>) instead of in the header or other objects
    # (that is because the technique consists in moving the target element and making it invisible). Markdown TOC
    # extension has no option to place targets as anchors instead of header IDs so we process the generated content
    # here to do that.
    processed_html_contents = html_contents
    for header_to_replace in re.compile(r"<h\d id=\".*\">.*</h\d>").findall(html_contents):
        header_id = header_to_replace.split('id="')[1].split('"')[0]
        header_level = header_to_replace.split('<h')[1].split(' ')[0]
        header_title = header_to_replace.split('">')[1].split('</')[0]
        header_plus_anchor = '<a name="{}"></a><h{}><a href="#{}">{}</a></h{}>'.format(
            header_id, header_level, header_id, header_title, header_level)
        processed_html_contents = processed_html_contents.replace(header_to_replace, header_plus_anchor)
    return mark_safe(processed_html_contents)


markdown.is_safe = True
register.filter(markdown)
