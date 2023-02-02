import os
import pprint

from __init__ import Gitconfig

config = Gitconfig(f"{os.getcwd()}/.git/config")
print("Parsed gitconfig: ")
pprint.pprint(config.loads())
