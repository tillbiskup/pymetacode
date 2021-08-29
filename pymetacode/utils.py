"""
utils module of the pymetacode package.
"""
import collections
import contextlib
import datetime
import os
import pkgutil
import re

import jinja2


def ensure_file_exists(name=''):
    """
    One sentence (on one line) describing the function.

    More description comes here...

    Parameters
    ----------
    name : :class:`str`
        Short description


    """
    if not name:
        raise ValueError('No filename given.')
    with open(name, 'a'):
        pass


def get_data_from_pkg_resources(name='', directory='templates'):
    """
    One sentence (on one line) describing the function.

    More description comes here...

    Parameters
    ----------
    name : :class:`str`
        Short description

    directory : :class:`str`
        Short description

    Returns
    -------
    contents : :class:`str`
        Short description


    """
    if not name:
        raise ValueError('No filename given.')
    contents = pkgutil.get_data(__package__, '/'.join([directory, name]))
    return contents


class ToDictMixin:
    """Mixin class for returning all public attributes as dict.

    Sometimes there is the need to either exclude public attributes (in case
    of infinite loops created by trying to apply ``to_dict`` in this case)
    or to add (public) attributes, particularly those used by getters and
    setters that are otherwise not included.

    To do so, there are two non_public attributes of this class each class
    inheriting from it will be able to set as well:

    * :attr:`_exclude_from_to_dict`
    * :attr:`_include_in_to_dict`

    The names should be rather telling. For details, see below.

    Attributes
    ----------
    __odict__ : :class:`collections.OrderedDict`
        Dictionary of attributes preserving the order of their definition

    _exclude_from_to_dict : :class:`list`
        Names of (public) attributes to exclude from dictionary

        Usually, the reason to exclude public attributes from being added to
        the dictionary is to avoid infinite loops, as sometimes an object
        may contain a reference to another object that in turn references back.

    _include_in_to_dict : :class:`list`
        Names of (public) attributes to include into dictionary

        Usual reasons for actively including (public) attributes into the
        dictionary are those attributes accessed by getters and setters and
        hence not automatically included in the list otherwise.

    """

    def __init__(self):
        if '__odict__' not in self.__dict__:
            self.__odict__ = collections.OrderedDict()
        self._exclude_from_to_dict = []
        self._include_in_to_dict = []

    def __setattr__(self, attribute, value):
        """
        Add attributes to :attr:`__odict__` to preserve order of definition.

        Parameters
        ----------
        attribute : :class:`str`
            Name of attribute
        value : :class:`str`
            Value of attribute

        """
        if '__odict__' not in self.__dict__:
            super().__setattr__('__odict__', collections.OrderedDict())
        self.__odict__[attribute] = value
        super().__setattr__(attribute, value)

    def to_dict(self):
        """
        Create dictionary containing public attributes of an object.

        Returns
        -------
        public_attributes : :class:`collections.OrderedDict`
            Ordered dictionary containing the public attributes of the object

            The order of attribute definition is preserved

        """
        if hasattr(self, '__odict__'):
            result = self._traverse_dict(self.__odict__)
        else:
            result = self._traverse_dict(self.__dict__)
        return result

    def _traverse_dict(self, instance_dict):
        output = collections.OrderedDict()
        for key, value in instance_dict.items():
            if str(key).startswith('_') \
                    or str(key) in self._exclude_from_to_dict:
                pass
            else:
                output[key] = self._traverse(key, value)
        for key in self._include_in_to_dict:
            output[key] = self._traverse(key, getattr(self, key))
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            result = value.to_dict()
        elif isinstance(value, (dict, collections.OrderedDict)):
            result = self._traverse_dict(value)
        elif hasattr(value, '__odict__'):
            result = self._traverse_dict(value.__odict__)
        elif hasattr(value, '__dict__'):
            result = self._traverse_dict(value.__dict__)
        elif isinstance(value, list):
            result = [self._traverse(key, i) for i in value]
        elif isinstance(value, (datetime.datetime, datetime.date,
                                datetime.time)):
            result = str(value)
        else:
            result = value
        return result


@contextlib.contextmanager
def change_working_dir(path=''):
    """
    One sentence (on one line) describing the function.

    More description comes here...

    Parameters
    ----------
    path : :class:`str`
        Short description

    """
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def camel_case_to_underscore(name=''):
    """
    One sentence (on one line) describing the function.

    More description comes here...

    Parameters
    ----------
    name : :class:`str`
        Short description

    Returns
    -------
    name : :class:`str`
        Short description

    """
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def underscore_to_camel_case(name=''):
    """
    One sentence (on one line) describing the function.

    More description comes here...

    Parameters
    ----------
    name : :class:`str`
        Short description

    Returns
    -------
    name : :class:`str`
        Short description

    """
    name = ''.join(char.capitalize() for char in name.split('_'))
    return name


class Template:
    """
    One sentence (on one line) describing the class.

    More description comes here...


    Attributes
    ----------
    package_path : :class:`str`
        Short description

    template : :class:`str`
        Short description

    context : :class:`dict`
        Short description

    destination : :class:`str`
        Short description

    Raises
    ------
    exception
        Short description when and why raised


    Examples
    --------

    It is always nice to give some examples how to use the class. Best to do
    that with code examples:

    .. code-block::

        template = Template()
        ...

    """

    def __init__(self, package_path='', template='', context=None,
                 destination=''):
        self.package_path = package_path
        self.template = template
        self.context = context
        self.destination = destination

    @property
    def environment(self):
        env = jinja2.Environment(
            loader=jinja2.PackageLoader(__package__,
                                        package_path=self.package_path),
            autoescape=jinja2.select_autoescape(),
            keep_trailing_newline=True,
        )
        return env

    def render(self):
        self._add_rst_markup_to_context()
        template = self.environment.get_template(self.template)
        return template.render(self.context)

    def create(self):
        with open(self.destination, 'w+') as file:
            file.write(self.render())

    def append(self):
        with open(self.destination, 'a') as file:
            file.write(self.render())

    def _add_rst_markup_to_context(self):
        if 'package' in self.context and 'name' in self.context['package']:
            rst_markup = {
                'header_hash': len(self.context['package']['name']) * '#',
                'header_equal': len(self.context['package']['name']) * '=',
                'header_minus': len(self.context['package']['name']) * '-',
                'header_tilde': len(self.context['package']['name']) * '~',
            }
            self.context['rst_markup'] = rst_markup
