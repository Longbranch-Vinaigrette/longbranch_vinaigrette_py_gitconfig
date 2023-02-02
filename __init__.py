from src.line import Line


class Gitconfig:
    def __init__(self, config_path: str):
        """Handler for Gitconfig files

        :param config_path: The path to .git/config or .gitmodules
        """
        self.config_path = config_path

    def parse(self, config: str):
        """Parse text from a gitconfig file"""
        raw_lines: list = config.splitlines()

        result: dict = {}
        last_region: str = ""
        for raw_line in raw_lines:
            # Pycharm doesn't detect that it's a string
            raw_line: str = raw_line
            line = Line(raw_line)
            print("Raw line: ", raw_line)
            if line.is_region():
                # Element is a region like:
                # [core]
                print("Element is a region.")
                result[raw_line]: dict = {}

                # Set last region
                last_region = raw_line
            else:
                # Element is a statement, like:
                #         url = git@github.com:Perseverancia-company/sub.gitconfig.git
                # (Yes they have tabs of 8 spaces)
                print("Element is not a region.")

                # Remove whitespace
                line_text = raw_line.strip()
                print("Line stripped: ", line_text)
                # Limit it to 1 just in case
                key, value = line_text.split(" = ", 1)
                print("Key: ", key)
                print("Its length: ", len(key))
                print("Value: ", value)
                print("Its length: ", len(value))

                if last_region:
                    # Insert it on the last_region zone
                    result[last_region][key] = value
                else:
                    # If there's no last_region, then insert it raw
                    result[key] = value

            print("\n")
        return result

    def loads(self) -> dict:
        """Converts a gitconfig file to a dictionary file"""
        with open(self.config_path) as f:
            raw_config: str = f.read()
        return self.parse(raw_config)

    def dumps(self):
        """Converts a dictionary to a gitconfig file

        It must be the same format as the one returned from loads"""

