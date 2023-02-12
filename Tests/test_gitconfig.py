import os
import unittest

from py_gitconfig import Gitconfig


class TestGitconfig(unittest.TestCase):
    def test_has_submodules(self):
        # Only if it's not being used as a submodule can we check this
        if os.path.isdir(f"{os.getcwd()}{os.path.sep}.git"):
            self.assertEqual(
                Gitconfig(os.getcwd()).has_submodules(),
                False
            )
