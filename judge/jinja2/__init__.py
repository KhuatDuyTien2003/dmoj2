import itertools
import json
from urllib.parse import quote

from jinja2.ext import Extension
from mptt.utils import get_cached_trees
from statici18n.templatetags.statici18n import inlinei18n

from judge.highlight_code import highlight_code
from judge.user_translations import gettext
try:
    from . import camo
except ImportError:
    camo = None

try:
    from . import datetime
except ImportError:
    datetime = None

try:
    from . import filesize
except ImportError:
    filesize = None

try:
    from . import format
except ImportError:
    format = None

try:
    from . import gravatar
except ImportError:
    gravatar = None

try:
    from . import language
except ImportError:
    language = None

try:
    from . import markdown
except ImportError:
    markdown = None

try:
    from . import rating
except ImportError:
    rating = None

try:
    from . import reference
except ImportError:
    reference = None

try:
    from . import render
except ImportError:
    render = None

try:
    from . import social
except ImportError:
    social = None

try:
    from . import spaceless
except ImportError:
    spaceless = None

try:
    from . import submission
except ImportError:
    submission = None

try:
    from . import timedelta
except ImportError:
    timedelta = None

from . import registry

registry.function('str', str)
registry.filter('str', str)
registry.filter('json', json.dumps)
registry.filter('highlight', highlight_code)
registry.filter('urlquote', quote)
registry.filter('roundfloat', round)
registry.function('inlinei18n', inlinei18n)
registry.function('mptt_tree', get_cached_trees)
registry.function('user_trans', gettext)


@registry.function
def counter(start=1):
    return itertools.count(start).__next__


class DMOJExtension(Extension):
    def __init__(self, env):
        super(DMOJExtension, self).__init__(env)
        env.globals.update(registry.globals)
        env.filters.update(registry.filters)
        env.tests.update(registry.tests)
