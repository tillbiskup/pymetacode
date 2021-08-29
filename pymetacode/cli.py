"""
cli module of the pymetacode package.
"""
import os.path
import shutil
import sys

from pymetacode import coding as coding, configuration as configuration


class Cli:
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

        obj = Cli()
        ...

    """

    def __init__(self):
        self.command = ''
        self.options = []
        self._command_name = 'pymeta'
        self.conf_file = 'package_config.yaml'

    def call(self, command='', options=None):
        self.command = command
        self.options = options
        if not self.command:
            self._print_help()
        else:
            method = '_command_{}'.format(self.command)
            if hasattr(self, method):
                getattr(self, method)()
            else:
                self._print_help()

    def _command_write(self):
        if not self.options or not self.options[0] == "config" \
                or (len(self.options) > 2 and not self.options[1] == "to"):
            self._print_write_help()
            return
        conf = configuration.Configuration()
        if len(self.options) == 3:
            self.conf_file = self.options[2]
        conf.to_file(self.conf_file)

    def _command_create(self):
        if not self.options or not self.options[0] == "package" \
                or not self.options[1] == "from":
            self._print_create_help()
            return
        conf_file = self.options[2]
        conf = configuration.Configuration()
        conf.from_file(conf_file)
        creator = coding.PackageCreator()
        creator.configuration = conf
        creator.name = conf.package['name']
        creator.create()
        shutil.copyfile(conf_file,
                        os.path.join(conf.package['name'],
                                     '.package_config.yaml'))
        print('Created package "{}" in directory "{}"'.format(
            conf.package['name'], conf.package['name']))

    def _command_add(self):
        if not self.options:
            self._print_add_help()
            return
        method = '_command_add_{}'.format(self.options[0])
        if hasattr(self, method):
            conf_file = '.package_config.yaml'
            conf = configuration.Configuration()
            conf.from_file(conf_file)
            getattr(self, method)(conf)
        else:
            self._print_add_help()

    def _command_add_module(self, conf):
        creator = coding.ModuleCreator()
        creator.configuration = conf
        creator.name = self.options[1]
        creator.create()
        print('Added module "{}"'.format(creator.name))

    def _command_add_class(self, conf):
        creator = coding.ClassCreator()
        creator.configuration = conf
        creator.name = self.options[1]
        creator.module = self.options[3]
        creator.create()
        print('Added class "{}" to module "{}"'.format(creator.name,
                                                       creator.module))

    def _command_add_function(self, conf):
        creator = coding.FunctionCreator()
        creator.configuration = conf
        creator.name = self.options[1]
        creator.module = self.options[3]
        creator.create()
        print('Added function "{}" to module "{}"'.format(creator.name,
                                                          creator.module))

    def _command_help(self):
        if not self.options:
            self._print_help()
        else:
            help_method = '_print_{}_help'.format(self.options[0])
            getattr(self, help_method)()

    def _print_help(self):
        help_text = """
        General usage:
            command_name <command> <option1> ...

        Possible commands are:
            write
            add
            create
            help

        To get more details for a command, type: 
            command_name help <command> 
        """
        self._output_help_text(help_text)

    def _print_write_help(self):
        help_text = """
        Usage for write command:
            command_name write <item> to <destination>
            command_name write <item>

        Possible items are:
            config

        Examples:
            command_name write config to package_config.yaml

            Writes a configuration file with empty values to 
            "package_config.yaml"

        Note: The default filename for the configuration file if not 
        provided is "package_config.yaml".          
        """
        self._output_help_text(help_text)

    def _print_create_help(self):
        help_text = """
        Usage for create command:
            command_name create package from <config>

        Prerequisite for this command is an existing configuration stored in 
        the file given as <config> (a YAML file). Use

            command_name write config to <filename>

        to create a config file in YAML format and populate the values 
        according to your needs. 
        """
        self._output_help_text(help_text)

    def _print_add_help(self):
        help_text = """
        Usage for add command:
            command_name add <item>
            command_name add <item> in <module>

        Possible items are:
            module
            class
            function

        For the latter two, you need to provide the name of an existing module 
        these items should be added to.
        """
        self._output_help_text(help_text)

    def _output_help_text(self, help_text=''):
        print(help_text.replace('        ', '').replace('command_name',
                                                        self._command_name))


def cli():
    """
    One sentence (on one line) describing the function.

    More description comes here...

    """
    cli_object = Cli()
    if len(sys.argv) == 1:
        cli_object.call()
    elif len(sys.argv) == 2:
        cli_object.call(command=sys.argv[1])
    else:
        cli_object.call(command=sys.argv[1], options=sys.argv[2:])

