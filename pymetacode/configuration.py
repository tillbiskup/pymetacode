"""
configuration module of the pymetacode package.
"""
import datetime

import oyaml as yaml

import pymetacode.utils as utils


class Configuration(utils.ToDictMixin):
    """
    One sentence (on one line) describing the class.

    More description comes here...


    Attributes
    ----------
    attr : :class:`None`
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

        obj = Configuration()
        ...


    .. versionadded:: 0.1

    """
    def __init__(self):
        super().__init__()
        self.package = {
            'name': '',
            'author': '',
            'author_email': '',
            'year': datetime.date.strftime(datetime.date.today(), '%Y'),
            'description': '',
            'urls': {
                'main': '',
                'documentation': '',
                'source': '',
            },
            'keywords': [],
            'install_requires': [],
            'git': False,
        }
        self.documentation = {
            'logo': '',
            'favicon': '',
        }

    def from_dict(self, dict_=None):
        """
        Set attributes from dictionary.

        Parameters
        ----------
        dict_ : :class:`dict`
            Dictionary containing information of a task.

        Raises
        ------
        aspecd.tasks.MissingDictError
            Raised if no dict is provided.

        """
        if not dict_:
            raise ValueError
        for key, value in dict_.items():
            if hasattr(self, key) and value:
                if isinstance(getattr(self, key), list):
                    if isinstance(value, list):
                        for element in value:
                            getattr(self, key).append(element)
                    else:
                        getattr(self, key).append(value)
                else:
                    setattr(self, key, value)

    def to_file(self, name=''):
        """
        Write to YAML file.

        Parameters
        ----------
        name : :class:`str`
            Name of the YAML file to write to.

        """
        with open(name, 'w+') as file:
            yaml.dump(self.to_dict(), file)

    def from_file(self, name=''):
        """
        Read from YAML file.

        Parameters
        ----------
        name : :class:`str`
            Name of the YAML file to read from.

        """
        with open(name, 'r') as file:
            dict_ = yaml.load(file, Loader=yaml.SafeLoader)
        self.from_dict(dict_)

