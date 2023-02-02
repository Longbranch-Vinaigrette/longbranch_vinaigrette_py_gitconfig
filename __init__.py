import re

from .src.line import Line


class Gitconfig:
    def __init__(self, config_path: str):
        """Handler for Gitconfig files

        :param config_path: The path to .git/config or .gitmodules
        """
        self.config_path = config_path

    def loads(self) -> dict:
        """Converts a gitconfig file to a dictionary file"""
        with open(self.config_path) as f:
            raw_config: str = f.read()
        raw_lines: list = raw_config.splitlines()

        result: dict = {}
        for raw_line in raw_lines:
            line = Line(raw_line)
            if line.is_region():
                # Element is a region like:
                # [core]
                print("Element is a region.")
                
            else:
                # Element is a statement, like:
                #         url = git@github.com:Perseverancia-company/sub.gitconfig.git
                # (Yes they have tabs of 8 spaces)
                print("Element is not a region.")
            print("\n")
        return result

    def dumps(self):
        """Converts a dictionary to a gitconfig file

        It must be the same format as the one returned from loads"""

