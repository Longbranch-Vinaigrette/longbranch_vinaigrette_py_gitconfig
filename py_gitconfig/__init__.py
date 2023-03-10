"""
Note: When dumping it doesn't seem to care about the order of the first keys, but I don't
consider this a problem for now, so I won't fix it.
"""
import os

from .line import Line


class Gitconfig:
    config_path: str = ""
    data: dict = {}
    regions: list = []

    def __init__(self, config_path: str):
        """Handler for Gitconfig files

        :param config_path: The path to .git/config or .gitmodules
        """
        # Check if it's a file, if it's set it raw
        if os.path.isfile(config_path):
            self.config_path = config_path
        else:
            # If it's a repository path then let's retrieve the config file
            git_folder = f"{config_path}{os.path.sep}.git"
            if os.path.isdir(git_folder):
                print("Is a git repository")
                # It's a repository
                actual_config_path = f"{config_path}{os.path.sep}" \
                                      f".git{os.path.sep}" \
                                      "config"
                self.config_path = actual_config_path
            else:
                # It's not a repository, raise exception
                raise Exception("Error: The given path is not a git config file "
                                "nor a repository.")

    def get_submodules_relative_path(self) -> list:
        """Get relative path"""
        submodules_paths: list = []
        self.data = self.loads()
        for key in list(self.data.keys()):
            line = Line(key)
            if line.is_submodule():
                try:
                    # This is a submodule
                    submodules_paths.append(self.data[key]["path"])
                except:
                    print("Warning: A submodule was found, but not its relative path, "
                          "it's likely that you provided the information on "
                          "./.git/config, but this file doesn't have the relative "
                          "paths of submodules, the one you need to provide is: "
                          "./.gitmodules")
        
        return submodules_paths

    def has_submodules(self) -> bool:
        """Check whether the repository uses submodules or not"""
        if not self.data:
            self.loads()

        for key in list(self.data.keys()):
            line = Line(key)
            if line.is_submodule():
                return True
        return False

    def parse(self, config: str) -> dict:
        """Parse text from a gitconfig file"""
        raw_lines: list = config.splitlines()

        result: dict = {}
        last_region: str = ""
        for raw_line in raw_lines:
            # Pycharm doesn't detect that it's a string
            raw_line: str = raw_line
            line = Line(raw_line)

            # Check whether the line is a region or not
            if line.is_region():
                # Element is a region like:
                # [core]
                result[raw_line]: dict = {}

                # Append to the region list
                self.regions.append(raw_line)

                # Set last region
                last_region = raw_line
            else:
                # Element is a statement, like:
                #         url = git@github.com:Perseverancia-company/sub.gitconfig.git
                # (Yes they have tabs of 8 spaces)

                # Remove whitespace
                line_text = raw_line.strip()

                # Limit it to 1 just in case
                key, value = line_text.split(" = ", 1)

                if last_region:
                    # Insert it on the last_region zone
                    result[last_region][key] = value
                else:
                    # If there's no last_region, then insert it raw
                    result[key] = value
        return result

    def loads(self) -> dict:
        """Converts a gitconfig file to a dictionary file"""
        with open(self.config_path) as f:
            raw_config: str = f.read()
        self.data = self.parse(raw_config)
        return self.data

    def encode(self, data: dict, inside_region: bool = False) -> str:
        """Encode a config dictionary"""
        result: str = ""
        for key in list(data.keys()):
            line = Line(key)

            # Check if it's a region or not
            if line.is_region():
                # Add and continue
                result += f"{key}\n"

                # Recurse over every field
                result += self.encode(data[key], inside_region=True)
            elif inside_region:
                # Add with whitespace
                result += f"{str(' ' * 8)}{key} = {str(data[key])}\n"
            else:
                # Add without whitespace
                result += f"{key} = {str(data[key])}\n"
        return result

    def dumps(self, path: str = ""):
        """Dump encoded gitconfig dictionary

        It uses the given path on instantiation"""
        gitconfig = self.encode(self.data)
        if not path:
            # Use the given path on instantiation
            with open(self.config_path, "w") as f:
                f.write(gitconfig)
        else:
            # Use the given path on function call
            with open(path, "w") as f:
                f.write(gitconfig)
        return gitconfig
