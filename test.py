import unittest


from Tests.test_line import TestSubmoduleRegion, TestRemoteRegion
from Tests.test_gitconfig import TestGitconfig

TestSubmoduleRegion()
TestRemoteRegion()
TestGitconfig()


if __name__ == "__main__":
    unittest.main()
