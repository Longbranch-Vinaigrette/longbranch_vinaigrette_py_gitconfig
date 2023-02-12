import unittest

from py_gitconfig.line import Line


# Submodule region
submodule_region = '[submodule "python_app_manager/longbranch_vinaigrette_py_repository_configuration"]'
submodule_line = Line(submodule_region)
print("Checking against: \n", submodule_region)


class TestSubmoduleRegion(unittest.TestCase):
    def test_is_submodule(self):
        self.assertEqual(
            submodule_line.is_submodule(),
            True
        )

    def test_submodule_region(self):
        self.assertEqual(
            submodule_line.is_region(),
            True
        )


# Check remote region
remote_region = '[remote "origin"]'
remote_line = Line(remote_region)
print("Checking againts: \n", remote_region)


class TestRemoteRegion(unittest.TestCase):
    def test_is_submodule(self):
        self.assertEqual(
            remote_line.is_submodule(),
            False
        )

    def test_is_region(self):
        self.assertEqual(
            remote_line.is_region(),
            True
        )
