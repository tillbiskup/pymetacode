"""
coding module of the pymetacode package.
"""
import os
import shutil
import subprocess
import warnings

from pymetacode import configuration as configuration, utils as utils


class PackageCreator:
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

        obj = PackageCreator()
        ...


    """

    def __init__(self):
        self.name = ''
        self.subdirectories = [
            'tests',
            os.path.join('docs', 'api'),
            'bin']
        self.configuration = configuration.Configuration()
        self.documentation = {
            'pages': ['audience', 'changelog', 'developers', 'installing',
                      'people', 'roadmap', 'usecases']
        }

    def create(self, name=''):
        if name:
            self.name = name
        elif not self.name:
            raise ValueError
        self._create_subdirectories()
        self._create_init_files()
        self._create_gitignore()
        self._create_version_file()
        self._create_license_file()
        self._create_setup_py_file()
        self._create_readme_file()
        self._create_version_updater_file()
        self._create_documentation_stub()
        self._git_init()

    def _create_subdirectories(self):
        self.subdirectories.append(self.name)
        for directory in self.subdirectories:
            self._create_directory(name=os.path.join(self.name, directory))

    @staticmethod
    def _create_directory(name=''):
        if os.path.exists(name):
            warnings.warn("Directory '" + name + "' exists already.")
        else:
            os.makedirs(name)

    def _create_init_files(self):
        for directory in [self.name, 'tests']:
            init_filename = os.path.join(self.name, directory, '__init__.py')
            utils.ensure_file_exists(init_filename)

    def _create_gitignore(self):
        contents = utils.get_data_from_pkg_resources('gitignore')
        with open(os.path.join(self.name, '.gitignore'), 'w+') as file:
            file.write(contents.decode("utf-8"))

    def _create_version_file(self):
        with open(os.path.join(self.name, 'VERSION'), 'w+') as file:
            file.write('0.1.0.dev0\n')

    def _create_license_file(self):
        template = utils.Template(
            package_path='templates/licenses',
            template='bsd-2clause.j2.txt',
            context=self.configuration.to_dict(),
            destination=os.path.join(self.name, 'LICENSE'),
        )
        template.create()

    def _create_setup_py_file(self):
        template = utils.Template(
            package_path='templates',
            template='setup.j2.py',
            context=self.configuration.to_dict(),
            destination=os.path.join(self.name, 'setup.py'),
        )
        template.create()

    def _create_readme_file(self):
        template = utils.Template(
            package_path='templates',
            template='README.j2.rst',
            context=self.configuration.to_dict(),
            destination=os.path.join(self.name, 'README.rst'),
        )
        template.create()

    def _create_version_updater_file(self):
        contents = utils.get_data_from_pkg_resources('incrementVersion.sh')
        destination = os.path.join(self.name, 'bin', 'incrementVersion.sh')
        with open(destination, 'w+') as file:
            file.write(contents.decode("utf-8"))

    def _create_documentation_stub(self):
        self._create_documentation_generator_files()
        self._create_documentation_config()
        self._create_documentation_index()
        self._create_documentation_api_index()
        self._create_documentation_contents()

    def _create_documentation_generator_files(self):
        make_files = ['make.bat', 'Makefile']
        for file in make_files:
            contents = \
                utils.get_data_from_pkg_resources('/'.join(['docs', file]))
            destination = os.path.join(self.name, 'docs', file)
            with open(destination, 'w+') as doc_file:
                doc_file.write(contents.decode("utf-8"))

    def _create_documentation_index(self):
        shutil.copyfile(
            os.path.join(self.name, 'README.rst'),
            os.path.join(self.name, 'docs', 'index.rst')
        )
        template = utils.Template(
            package_path='templates/docs',
            template='main-toctree.j2.rst',
            context=self.configuration.to_dict(),
            destination=os.path.join(self.name, 'docs', 'index.rst'),
        )
        template.append()

    def _create_documentation_config(self):
        template = utils.Template(
            package_path='templates/docs',
            template='conf.j2.py',
            context=self.configuration.to_dict(),
            destination=os.path.join(self.name, 'docs', 'conf.py'),
        )
        template.create()

    def _create_documentation_api_index(self):
        template = utils.Template(
            package_path='templates/docs',
            template='api_index.j2.rst',
            context=self.configuration.to_dict(),
            destination=os.path.join(self.name, 'docs', 'api', 'index.rst'),
        )
        template.create()

    def _create_documentation_contents(self):
        for name in self.documentation['pages']:
            template = utils.Template(
                package_path='templates/docs',
                template='{}.j2.rst'.format(name),
                context=self.configuration.to_dict(),
                destination=os.path.join(self.name, 'docs',
                                         '{}.rst'.format(name)),
            )
            template.create()

    def _git_init(self):
        if self.configuration.package['git']:
            subprocess.run(["git", "init"], cwd=self.name)
            with utils.change_working_dir(os.path.join(self.name, '.git',
                                                       'hooks')):
                with open('pre-commit', 'w+') as file:
                    file.write('#!/bin/sh\n')
                    file.write('./bin/incrementVersion.sh\n')
                shutil.copymode('pre-commit.sample', 'pre-commit')


class ModuleCreator:
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

        obj = ModuleCreator()
        ...


    """

    def __init__(self):
        self.name = ''
        self.configuration = configuration.Configuration()

    def create(self, name=''):
        if name:
            self.name = name
        elif not self.name:
            raise ValueError
        self._create_module()
        self._create_test_module()
        self._create_api_documentation()
        self._add_api_documentation_to_toctree()

    def _create_module(self):
        filename = os.path.join(self.configuration.package['name'],
                                self.name + '.py')
        if os.path.exists(filename):
            warnings.warn("Module '{}' exists already".format(filename))
            return
        context = self.configuration.to_dict()
        context['module'] = {'name': self.name}
        template = utils.Template(
            package_path='templates/code',
            template='module.j2.py',
            context=context,
            destination=filename,
        )
        template.create()

    def _create_test_module(self):
        filename = os.path.join('tests', 'test_{}.py'.format(self.name))
        if os.path.exists(filename):
            warnings.warn("Module '{}' exists already".format(filename))
            return
        context = self.configuration.to_dict()
        context['module'] = {'name': self.name}
        template = utils.Template(
            package_path='templates/code',
            template='test_module.j2.py',
            context=context,
            destination=filename,
        )
        template.create()

    def _create_api_documentation(self):
        package = self.configuration.package['name']
        filename = os.path.join('docs', 'api', '{}.{}.rst'.format(package,
                                                                  self.name))
        if os.path.exists(filename):
            warnings.warn("File '{}' exists already".format(filename))
            return
        context = self.configuration.to_dict()
        context['module'] = {'name': self.name}
        context['header_extension'] = \
            (len(package) + len(self.name) + 1) * '='
        template = utils.Template(
            package_path='templates/docs',
            template='api_module.j2.rst',
            context=context,
            destination=filename,
        )
        template.create()

    def _add_api_documentation_to_toctree(self):
        index_filename = os.path.join('docs', 'api', 'index.rst')
        if not os.path.exists(index_filename):
            return
        with open(index_filename) as file:
            contents = file.read()
        lines = contents.split('\n')
        package = self.configuration.package['name']
        start_of_toctree = lines.index('.. toctree::')
        end_of_toctree = lines[start_of_toctree:].index('')
        lines.insert(start_of_toctree + end_of_toctree + 1,
                     '    {}.{}'.format(package, self.name))
        with open(index_filename, "w+") as file:
            file.write('\n'.join(lines))


class ClassCreator:
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

        obj = ClassCreator()
        ...


    """
    def __init__(self):
        self.name = ''
        self.module = ''
        self.configuration = configuration.Configuration()

    def create(self, name='', module=''):
        if name:
            self.name = name
        elif not self.name:
            raise ValueError('Class name missing')
        if module:
            self.module = module
        elif not self.module:
            raise ValueError('Module name missing')
        package = self.configuration.package['name']
        if not os.path.exists(os.path.join(package, '{}.py'.format(
                self.module))):
            raise ValueError('Module {} does not exist', self.module)
        self._create_class()
        self._create_test_class()

    def _create_class(self):
        context = self.configuration.to_dict()
        context['class'] = {'name': self.name}
        package = self.configuration.package['name']
        filename = os.path.join(package, '{}.py'.format(self.module))
        template = utils.Template(
            package_path='templates/code',
            template='class.j2.py',
            context=context,
            destination=filename,
        )
        template.append()

    def _create_test_class(self):
        context = self.configuration.to_dict()
        context['class'] = {
            'name': self.name,
            'instance': utils.camel_case_to_underscore(self.name),
        }
        context['module'] = {'name': self.module}
        filename = os.path.join('tests', 'test_{}.py'.format(self.module))
        template = utils.Template(
            package_path='templates/code',
            template='test_class.j2.py',
            context=context,
            destination=filename,
        )
        template.append()


class FunctionCreator:
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

        obj = FunctionCreator()
        ...


    """
    def __init__(self):
        self.name = ''
        self.module = ''
        self.configuration = configuration.Configuration()

    def create(self, name='', module=''):
        if name:
            self.name = name
        elif not self.name:
            raise ValueError('Function name missing')
        if module:
            self.module = module
        elif not self.module:
            raise ValueError('Module name missing')
        package = self.configuration.package['name']
        if not os.path.exists(os.path.join(package, '{}.py'.format(
                self.module))):
            raise ValueError('Module {} does not exist', self.module)
        self._create_function()
        self._create_test_class()

    def _create_function(self):
        context = self.configuration.to_dict()
        context['function'] = {'name': self.name}
        package = self.configuration.package['name']
        filename = os.path.join(package, '{}.py'.format(self.module))
        template = utils.Template(
            package_path='templates/code',
            template='function.j2.py',
            context=context,
            destination=filename,
        )
        template.append()

    def _create_test_class(self):
        context = self.configuration.to_dict()
        context['function'] = {
            'name': self.name,
            'name_camelcase': utils.underscore_to_camel_case(self.name),
        }
        context['module'] = {'name': self.module}
        filename = os.path.join('tests', 'test_{}.py'.format(self.module))
        template = utils.Template(
            package_path='templates/code',
            template='test_function.j2.py',
            context=context,
            destination=filename,
        )
        template.append()
