import contextlib
import io
import os
import shutil
import subprocess
import unittest

from pymetacode import cli,configuration,utils


class TestCli(unittest.TestCase):

    def setUp(self):
        self.cli = cli.Cli()
        self.config_filename = 'package_config.yaml'
        self.package_name = 'foo'

    def tearDown(self):
        if os.path.exists(self.config_filename):
            os.remove(self.config_filename)
        if os.path.exists(self.package_name):
            shutil.rmtree(self.package_name)

    def test_instantiate_class(self):
        pass

    def test_call_with_command_sets_command_property(self):
        command = "help"
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command=command)
        self.assertEqual(command, self.cli.command)

    def test_call_with_options_sets_options_property(self):
        options = "config"
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(options=options)
        self.assertEqual(options, self.cli.options)

    def test_call_without_command_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call()
        content = stdout.getvalue()
        self.assertIn('General usage:', content)

    def test_call_with_unknown_command_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="foo")
        content = stdout.getvalue()
        self.assertIn('General usage:', content)

    def test_call_with_help_command_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="help")
        content = stdout.getvalue()
        self.assertIn('General usage:', content)

    def test_call_help_write_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="help", options=["write"])
        content = stdout.getvalue()
        self.assertIn('Usage for write command:', content)

    def test_call_help_create_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="help", options=["create"])
        content = stdout.getvalue()
        self.assertIn('Usage for create command:', content)

    def test_call_help_add_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="help", options=["add"])
        content = stdout.getvalue()
        self.assertIn('Usage for add command:', content)

    def test_call_write_writes_config(self):
        self.cli.call(command="write",
                      options=["config", "to", self.config_filename])
        self.assertTrue(os.path.exists(self.config_filename))

    def test_call_write_with_wrong_options_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="write",
                          options=["foo", "bar", self.config_filename])
        content = stdout.getvalue()
        self.assertIn('Usage for write command:', content)
        self.assertFalse(os.path.exists(self.config_filename))

    def test_call_write_without_options_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="write")
        content = stdout.getvalue()
        self.assertIn('Usage for write command:', content)
        self.assertFalse(os.path.exists(self.config_filename))

    def test_call_write_config_without_destination_uses_default_name(self):
        self.cli.call(command="write",
                      options=["config"])
        self.assertTrue(os.path.exists(self.config_filename))

    def test_call_create_creates_package(self):
        conf = configuration.Configuration()
        conf.package['name'] = self.package_name
        conf.to_file(self.config_filename)
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        self.assertTrue(os.path.exists(
            os.path.join(self.package_name, self.package_name)))

    def test_call_create_copies_package_config_to_package(self):
        conf = configuration.Configuration()
        conf.package['name'] = self.package_name
        conf.to_file(self.config_filename)
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        self.assertTrue(os.path.exists(
            os.path.join(self.package_name, '.package_config.yaml')))

    def test_call_create_with_wrong_options_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="create",
                          options=["foo", "bar", self.config_filename])
        content = stdout.getvalue()
        self.assertIn('Usage for create command:', content)
        self.assertFalse(os.path.exists(
            os.path.join(self.package_name, self.package_name)))

    def test_call_create_without_options_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="create")
        content = stdout.getvalue()
        self.assertIn('Usage for create command:', content)
        self.assertFalse(os.path.exists(
            os.path.join(self.package_name, self.package_name)))

    def test_call_create_prints_success_message(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            conf = configuration.Configuration()
            conf.package['name'] = self.package_name
            conf.to_file(self.config_filename)
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        content = stdout.getvalue()
        self.assertIn('Created package "{}" in directory "{}"'.format(
            self.package_name, self.package_name), content)

    def test_call_add_module_adds_module(self):
        conf = configuration.Configuration()
        conf.package['name'] = self.package_name
        conf.to_file(self.config_filename)
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        with utils.change_working_dir(self.package_name):
            module_name = "bar"
            with contextlib.redirect_stdout(io.StringIO()):
                self.cli.call(command="add",
                              options=["module", module_name])
            self.assertTrue(os.path.exists(
                os.path.join(self.package_name, module_name + '.py')))

    def test_call_add_module_prints_success_message(self):
        conf = configuration.Configuration()
        conf.package['name'] = self.package_name
        conf.to_file(self.config_filename)
        with contextlib.redirect_stdout(io.StringIO()):
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        with utils.change_working_dir(self.package_name):
            module_name = "bar"
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                self.cli.call(command="add",
                              options=["module", module_name])
        content = stdout.getvalue()
        self.assertIn('Added module "{}"'.format(module_name), content)

    def test_call_add_with_wrong_options_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="add",
                          options=["foo", "module_name"])
        content = stdout.getvalue()
        self.assertIn('Usage for add command:', content)

    def test_call_add_without_options_prints_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.cli.call(command="add")
        content = stdout.getvalue()
        self.assertIn('Usage for add command:', content)

    def test_call_add_class_adds_class(self):
        conf = configuration.Configuration()
        conf.package['name'] = self.package_name
        conf.to_file(self.config_filename)
        with contextlib.redirect_stdout(io.StringIO()):
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        with utils.change_working_dir(self.package_name):
            class_name = "FooBar"
            module_name = "bar"
            with contextlib.redirect_stdout(io.StringIO()):
                self.cli.call(command="add",
                              options=["module", module_name])
                self.cli.call(command="add",
                              options=["class", class_name, "to", module_name])
            module_path = os.path.join(self.package_name, module_name + '.py')
            with open(module_path) as file:
                contents = file.read()
            self.assertIn('class {}:\n'.format(class_name), contents)

    def test_call_add_class_prints_success_message(self):
        conf = configuration.Configuration()
        conf.package['name'] = self.package_name
        conf.to_file(self.config_filename)
        with contextlib.redirect_stdout(io.StringIO()):
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        with utils.change_working_dir(self.package_name):
            class_name = "FooBar"
            module_name = "bar"
            with contextlib.redirect_stdout(io.StringIO()):
                self.cli.call(command="add",
                              options=["module", module_name])
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                self.cli.call(command="add",
                              options=["class", class_name, "to", module_name])
        content = stdout.getvalue()
        self.assertIn('Added class "{}" to module "{}"'.format(
            class_name, module_name), content)

    def test_call_add_function_adds_function(self):
        conf = configuration.Configuration()
        conf.package['name'] = self.package_name
        conf.to_file(self.config_filename)
        with contextlib.redirect_stdout(io.StringIO()):
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        with utils.change_working_dir(self.package_name):
            function_name = "foo_bar"
            module_name = "bar"
            with contextlib.redirect_stdout(io.StringIO()):
                self.cli.call(command="add",
                              options=["module", module_name])
                self.cli.call(command="add",
                              options=["function", function_name, "to",
                                       module_name])
            module_path = os.path.join(self.package_name, module_name + '.py')
            with open(module_path) as file:
                contents = file.read()
            self.assertIn('def {}():\n    """'.format(function_name), contents)

    def test_call_add_function_prints_success_message(self):
        conf = configuration.Configuration()
        conf.package['name'] = self.package_name
        conf.to_file(self.config_filename)
        with contextlib.redirect_stdout(io.StringIO()):
            self.cli.call(command="create",
                          options=["package", "from", self.config_filename])
        with utils.change_working_dir(self.package_name):
            function_name = "foo_bar"
            module_name = "bar"
            with contextlib.redirect_stdout(io.StringIO()):
                self.cli.call(command="add",
                              options=["module", module_name])
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                self.cli.call(command="add",
                              options=["function", function_name, "to",
                                       module_name])
        content = stdout.getvalue()
        self.assertIn('Added function "{}" to module "{}"'.format(
            function_name, module_name), content)


class TestConsoleEntryPoint(unittest.TestCase):

    def test_call_without_command_prints_help(self):
        result = subprocess.run(["pymeta"], capture_output=True, text=True)
        self.assertIn('General usage:', result.stdout)

    def test_call_help_prints_help(self):
        result = subprocess.run(["pymeta", "help"],
                                capture_output=True, text=True)
        self.assertIn('General usage:', result.stdout)

    def test_call_help_write_prints_help(self):
        result = subprocess.run(["pymeta", "help", "write"],
                                capture_output=True, text=True)
        self.assertIn('Usage for write command:', result.stdout)
