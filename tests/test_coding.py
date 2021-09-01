import datetime
import os
import shutil
import unittest
import warnings

from pymetacode import coding, utils
import pymetacode.configuration


class TestPackageCreator(unittest.TestCase):

    def setUp(self):
        self.creator = coding.PackageCreator()
        self.name = 'foo'

    def tearDown(self):
        if os.path.exists(self.name):
            shutil.rmtree(self.name)

    def test_instantiate_class(self):
        pass

    def test_has_create_method(self):
        self.assertTrue(hasattr(self.creator, 'create'))
        self.assertTrue(callable(self.creator.create))

    def test_create_without_name_raises(self):
        with self.assertRaises(ValueError):
            self.creator.create()

    def test_create_with_name_property_set(self):
        self.creator.name = self.name
        self.creator.create()

    def test_create_with_name_sets_name_property(self):
        self.creator.create(name=self.name)
        self.assertEqual(self.name, self.creator.name)

    def test_create_creates_package_directory(self):
        self.creator.create(name=self.name)
        self.assertTrue(os.path.exists(self.name))
        self.assertTrue(os.path.isdir(self.name))

    def test_create_with_existing_directory_issues_warning(self):
        os.makedirs(os.path.join(self.name, self.name))
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            self.creator.create(name=self.name)
            self.assertTrue(w)
        self.assertTrue(os.path.exists(self.name))
        self.assertTrue(os.path.isdir(self.name))

    def test_create_creates_subdirectories(self):
        directories = [
            os.path.join(self.name, self.name),
            os.path.join(self.name, 'tests'),
            os.path.join(self.name, 'docs', 'api'),
            os.path.join(self.name, 'bin'),
        ]
        self.creator.create(name=self.name)
        for directory in directories:
            with self.subTest(directory=directory):
                self.assertTrue(os.path.exists(directory))
                self.assertTrue(os.path.isdir(directory))

    def test_create_creates_init_files(self):
        directories = [
            os.path.join(self.name, self.name),
            os.path.join(self.name, 'tests'),
        ]
        self.creator.create(name=self.name)
        for directory in directories:
            with self.subTest(directory=directory):
                filename = os.path.join(directory, '__init__.py')
                self.assertTrue(os.path.exists(filename))

    def test_create_copies_gitignore_file(self):
        self.creator.create(name=self.name)
        self.assertTrue(os.path.exists(os.path.join(self.name, '.gitignore')))

    def test_create_creates_version_file(self):
        self.creator.create(name=self.name)
        self.assertTrue(os.path.exists(os.path.join(self.name, 'VERSION')))

    def test_create_sets_version_in_version_file(self):
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'VERSION')) as file:
            contents = file.read().strip()
        self.assertEqual('0.1.0.dev0', contents)

    def test_create_creates_license_file(self):
        self.creator.create(name=self.name)
        self.assertTrue(os.path.exists(os.path.join(self.name, 'LICENSE')))

    def test_create_fills_license_file(self):
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'LICENSE')) as file:
            contents = file.read()
        self.assertIn('THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT', contents)

    def test_create_replaces_placeholders_in_license_file(self):
        configuration = pymetacode.configuration.Configuration()
        configuration.package['author'] = 'John Doe'
        self.creator.configuration = configuration
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'LICENSE')) as file:
            contents = file.read()
        current_year = datetime.date.strftime(datetime.date.today(), '%Y')
        copyright_line = \
            'Copyright (c) {} {}'.format(current_year,
                                         configuration.package['author'])
        self.assertIn(copyright_line, contents)

    def test_create_creates_setup_py_file(self):
        self.creator.create(name=self.name)
        self.assertTrue(os.path.exists(os.path.join(self.name, 'setup.py')))

    def test_create_fills_setup_py_file(self):
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'setup.py')) as file:
            contents = file.read()
        self.assertIn('setuptools.setup(', contents)

    def test_create_replaces_placeholders_in_setup_py_file(self):
        configuration = pymetacode.configuration.Configuration()
        configuration.package['author'] = 'John Doe'
        self.creator.configuration = configuration
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'setup.py')) as file:
            contents = file.read()
        content_line = "author='{}'".format(configuration.package['author'])
        self.assertIn(content_line, contents)

    def test_create_creates_readme_file(self):
        self.creator.create(name=self.name)
        self.assertTrue(os.path.exists(os.path.join(self.name, 'README.rst')))

    def test_create_fills_readme_file(self):
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'README.rst')) as file:
            contents = file.read()
        self.assertIn('documentation', contents)

    def test_create_replaces_placeholders_in_readme_file(self):
        configuration = pymetacode.configuration.Configuration()
        configuration.package['name'] = self.name
        self.creator.configuration = configuration
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'README.rst')) as file:
            contents = file.read()
        content_line = "{} documentation".format(self.name)
        self.assertIn(content_line, contents)

    def test_create_readme_file_adjusts_rst_header_length(self):
        configuration = pymetacode.configuration.Configuration()
        configuration.package['name'] = self.name
        self.creator.configuration = configuration
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'README.rst')) as file:
            contents = file.read().split('\n')
        self.assertEqual(len(contents[0]), len(contents[1]))

    def test_create_creates_version_updater_file(self):
        self.creator.create(name=self.name)
        self.assertTrue(os.path.exists(
            os.path.join(self.name, 'bin', 'incrementVersion.sh')))

    def test_create_fills_version_updater_file(self):
        self.creator.create(name=self.name)
        file_path = os.path.join(self.name, 'bin', 'incrementVersion.sh')
        with open(file_path) as file:
            contents = file.read()
        self.assertIn('Increment version number', contents)

    def test_version_updater_is_executable(self):
        self.creator.create(name=self.name)
        file_path = os.path.join(self.name, 'bin', 'incrementVersion.sh')
        self.assertTrue(os.access(file_path, os.X_OK))

    def test_create_populates_docs_subdirectory(self):
        self.creator.create(name=self.name)
        files = ['make.bat', 'Makefile', 'index.rst', 'conf.py']
        for file in files:
            with self.subTest(file=file):
                filename = os.path.join(self.name, 'docs', file)
                self.assertTrue(os.path.exists(filename))

    def test_create_adds_toctree_to_documentation_index(self):
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'docs', 'index.rst')) as file:
            contents = file.read()
        self.assertIn('.. toctree::', contents)

    def test_create_populates_docs_api_subdirectory(self):
        self.creator.create(name=self.name)
        files = ['index.rst']
        for file in files:
            with self.subTest(file=file):
                filename = os.path.join(self.name, 'docs', 'api', file)
                self.assertTrue(os.path.exists(filename))

    def test_create_populates_docs_directory(self):
        self.creator.create(name=self.name)
        files = self.creator.documentation['pages']
        for file in files:
            with self.subTest(file=file):
                filename = os.path.join(self.name, 'docs',
                                        '{}.rst'.format(file))
                self.assertTrue(os.path.exists(filename))

    def test_create_replaces_placeholders_in_docs_conf_file(self):
        configuration = pymetacode.configuration.Configuration()
        configuration.package['name'] = self.name
        self.creator.configuration = configuration
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, 'docs', 'conf.py')) as file:
            contents = file.read()
        self.assertIn(self.name, contents)

    def test_create_with_git_true_creates_git_directory(self):
        configuration = pymetacode.configuration.Configuration()
        configuration.package['name'] = self.name
        configuration.package['git'] = True
        self.creator.configuration = configuration
        self.creator.create(name=self.name)
        self.assertTrue(os.path.exists(os.path.join(self.name, '.git')))

    def test_create_with_git_true_creates_pre_commit_hook(self):
        configuration = pymetacode.configuration.Configuration()
        configuration.package['name'] = self.name
        configuration.package['git'] = True
        self.creator.configuration = configuration
        self.creator.create(name=self.name)
        with open(os.path.join(self.name, '.git', 'hooks', 'pre-commit')) as \
                file:
            content = file.read()
        self.assertIn('./bin/incrementVersion.sh', content)
        self.assertTrue(os.access(os.path.join(self.name, '.git', 'hooks',
                                               'pre-commit'), os.X_OK))


class TestModuleCreator(unittest.TestCase):

    def setUp(self):
        self.creator = coding.ModuleCreator()
        self.package = 'bar'
        self.name = 'foo'
        self.configuration = pymetacode.configuration.Configuration()
        self.configuration.package['name'] = self.package
        self.creator.configuration = self.configuration
        self.create_package_structure()

    def tearDown(self):
        if os.path.exists(self.configuration.package['name']):
            shutil.rmtree(self.configuration.package['name'])
        if os.path.exists('tests'):
            shutil.rmtree('tests')
        if os.path.exists('docs'):
            shutil.rmtree('docs')

    def create_package_structure(self):
        os.mkdir(self.configuration.package['name'])
        os.mkdir('tests')
        os.makedirs(os.path.join('docs', 'api'))

    def test_instantiate_class(self):
        pass

    def test_has_create_method(self):
        self.assertTrue(hasattr(self.creator, 'create'))
        self.assertTrue(callable(self.creator.create))

    def test_create_without_name_raises(self):
        with self.assertRaises(ValueError):
            self.creator.create()

    def test_create_with_name_property_set(self):
        self.creator.name = self.name
        self.creator.create()

    def test_create_with_name_sets_name_property(self):
        self.creator.create(name=self.name)
        self.assertEqual(self.name, self.creator.name)

    def test_create_creates_module(self):
        self.creator.create(name=self.name)
        path = os.path.join(self.package, self.name + '.py')
        self.assertTrue(os.path.exists(path))

    def test_create_with_name_property_set_creates_module(self):
        self.creator.name = self.name
        self.creator.create()
        path = os.path.join(self.package, self.name + '.py')
        self.assertTrue(os.path.exists(path))

    def test_create_does_not_change_existing_file(self):
        filename = os.path.join(self.package, self.name + '.py')
        with open(filename, 'a') as file:
            file.write('foo bar')
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.creator.create(name=self.name)
        with open(filename) as file:
            file_content = file.read()
        self.assertEqual('foo bar', file_content)

    def test_create_warns_if_module_exists(self):
        filename = os.path.join(self.package, self.name + '.py')
        with open(filename, 'a') as file:
            file.write('foo bar')
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            self.creator.create(name=self.name)
            self.assertTrue(w)

    def test_create_replaces_placeholders_in_module_file(self):
        filename = os.path.join(self.package, self.name + '.py')
        self.creator.create(name=self.name)
        with open(filename) as file:
            contents = file.read()
        content_line = \
            '{} module of the {} package.'.format(self.name, self.package)
        self.assertIn(content_line, contents)

    def test_create_creates_test_module(self):
        self.creator.create(name=self.name)
        path = os.path.join('tests', 'test_{}.py'.format(self.name))
        self.assertTrue(os.path.exists(path))

    def test_create_with_name_property_set_creates_test_module(self):
        self.creator.name = self.name
        self.creator.create()
        path = os.path.join('tests', 'test_{}.py'.format(self.name))
        self.assertTrue(os.path.exists(path))

    def test_create_does_not_change_existing_test_file(self):
        filename = os.path.join(self.package, 'test_{}.py'.format(self.name))
        with open(filename, 'a') as file:
            file.write('foo bar')
        self.creator.create(name=self.name)
        with open(filename) as file:
            file_content = file.read()
        self.assertEqual('foo bar', file_content)

    def test_create_warns_if_test_module_exists(self):
        filename = os.path.join('tests', 'test_{}.py'.format(self.name))
        with open(filename, 'a') as file:
            file.write('foo bar')
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            self.creator.create(name=self.name)
            self.assertTrue(w)

    def test_create_replaces_placeholders_in_test_module_file(self):
        filename = os.path.join('tests', 'test_{}.py'.format(self.name))
        self.creator.create(name=self.name)
        with open(filename) as file:
            contents = file.read()
        content_line = 'from {} import {}'.format(self.package, self.name)
        self.assertIn(content_line, contents)

    def test_create_creates_api_documentation(self):
        self.creator.create(name=self.name)
        filename = os.path.join('docs', 'api', '{}.{}.rst'.format(self.package,
                                                                  self.name))
        self.assertTrue(os.path.exists(filename))

    def test_create_warns_if_api_documentation_exists(self):
        filename = os.path.join('docs', 'api', '{}.{}.rst'.format(self.package,
                                                                  self.name))
        with open(filename, 'a') as file:
            file.write('foo bar')
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            self.creator.create(name=self.name)
            self.assertTrue(w)

    def test_create_replaces_placeholders_in_api_documentation(self):
        filename = os.path.join('docs', 'api', '{}.{}.rst'.format(self.package,
                                                                  self.name))
        self.creator.create(name=self.name)
        with open(filename) as file:
            contents = file.read()
        content_line = \
            '{}.{} module'.format(self.package, self.name)
        self.assertIn(content_line, contents)

    def test_create_adds_documentation_to_api_toctree(self):
        index_filename = os.path.join('docs', 'api', 'index.rst')
        index_contents = """

        .. toctree::
            :maxdepth: 1



        Index
        -----
        """.replace('        ', '')
        with open(index_filename, 'w+') as file:
            file.write(index_contents)
        self.creator.create(name=self.name)
        toctree_entry = '{}.{}'.format(self.package, self.name)
        with open(index_filename) as file:
            contents = file.read()
        self.assertIn(toctree_entry, contents)


class TestClassCreator(unittest.TestCase):

    def setUp(self):
        self.creator = coding.ClassCreator()
        self.package = 'bar'
        self.module = 'foo'
        self.name = 'FooBar'
        self.configuration = pymetacode.configuration.Configuration()
        self.configuration.package['name'] = self.package
        self.creator.configuration = self.configuration
        self.create_package_structure()
        self.create_module()

    def tearDown(self):
        if os.path.exists(self.configuration.package['name']):
            shutil.rmtree(self.configuration.package['name'])
        if os.path.exists('tests'):
            shutil.rmtree('tests')
        if os.path.exists('docs'):
            shutil.rmtree('docs')

    def create_package_structure(self):
        os.mkdir(self.configuration.package['name'])
        os.mkdir('tests')
        os.makedirs(os.path.join('docs', 'api'))

    def create_module(self):
        creator = coding.ModuleCreator()
        creator.name = self.module
        creator.configuration = self.configuration
        creator.create()

    def test_instantiate_class(self):
        pass

    def test_has_create_method(self):
        self.assertTrue(hasattr(self.creator, 'create'))
        self.assertTrue(callable(self.creator.create))

    def test_create_without_name_raises(self):
        with self.assertRaises(ValueError):
            self.creator.create()

    def test_create_without_module_raises(self):
        with self.assertRaises(ValueError):
            self.creator.create(name='foo')

    def test_create_with_nonexisting_module_raises(self):
        with self.assertRaises(ValueError):
            self.creator.create(name='foo', module='foofoofoofoofoo')

    def test_create_creates_class_in_module(self):
        self.creator.create(name=self.name, module=self.module)
        path = os.path.join(self.package, self.module + '.py')
        with open(path) as file:
            contents = file.read()
        self.assertIn('class {}:\n    """'.format(self.name), contents)

    def test_create_creates_test_class_in_test_module(self):
        self.creator.create(name=self.name, module=self.module)
        path = os.path.join('tests', 'test_{}.py'.format(self.module))
        with open(path) as file:
            contents = file.read()
        self.assertIn('class Test{}(unittest.TestCase):'.format(self.name),
                      contents)


class TestFunctionCreator(unittest.TestCase):

    def setUp(self):
        self.creator = coding.FunctionCreator()
        self.package = 'bar'
        self.module = 'foo'
        self.name = 'foo_bar'
        self.configuration = pymetacode.configuration.Configuration()
        self.configuration.package['name'] = self.package
        self.creator.configuration = self.configuration
        self.create_package_structure()
        self.create_module()

    def tearDown(self):
        if os.path.exists(self.configuration.package['name']):
            shutil.rmtree(self.configuration.package['name'])
        if os.path.exists('tests'):
            shutil.rmtree('tests')
        if os.path.exists('docs'):
            shutil.rmtree('docs')

    def create_package_structure(self):
        os.mkdir(self.configuration.package['name'])
        os.mkdir('tests')
        os.makedirs(os.path.join('docs', 'api'))

    def create_module(self):
        creator = coding.ModuleCreator()
        creator.name = self.module
        creator.configuration = self.configuration
        creator.create()

    def test_instantiate_class(self):
        pass

    def test_has_create_method(self):
        self.assertTrue(hasattr(self.creator, 'create'))
        self.assertTrue(callable(self.creator.create))

    def test_create_without_name_raises(self):
        with self.assertRaises(ValueError):
            self.creator.create()

    def test_create_without_module_raises(self):
        with self.assertRaises(ValueError):
            self.creator.create(name='foo')

    def test_create_with_nonexisting_module_raises(self):
        with self.assertRaises(ValueError):
            self.creator.create(name='foo', module='foofoofoofoofoo')

    def test_create_creates_function_in_module(self):
        self.creator.create(name=self.name, module=self.module)
        path = os.path.join(self.package, self.module + '.py')
        with open(path) as file:
            contents = file.read()
        self.assertIn('def {}():\n    """'.format(self.name), contents)

    def test_create_creates_test_class_in_test_module(self):
        self.creator.create(name=self.name, module=self.module)
        path = os.path.join('tests', 'test_{}.py'.format(self.module))
        with open(path) as file:
            contents = file.read()
        camel = utils.underscore_to_camel_case(self.name)
        self.assertIn('class Test{}(unittest.TestCase):'.format(camel),
                      contents)
