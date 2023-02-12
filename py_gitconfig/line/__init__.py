import re


class Line:
    def __init__(self, line: str):
        self.line = line

    def is_region(self):
        """Check if the line is a region or not

        Regions look like this: [core]"""
        return True if re.match(r"\[([a-z]|[0-9]|\"| |_|.|-|\||:|,|\(|\)|\')+]",
                        self.line) else False

    def is_submodule(self):
        """Check if the region is a submodule"""
        return True if re.match(r"\[submodule \"([a-z]|[0-9]|\"| |_|.|-|\||:|,|\(|\)|\')+\"]",
                        self.line) else False
