import re


class Line:
    def __init__(self, line: str):
        self.line = line

    def is_region(self):
        """Check if the line is a region or not

        Regions look like this: [core]"""
        return re.match(r"\[([a-z]|[0-9]|\"| )+]", self.line)
