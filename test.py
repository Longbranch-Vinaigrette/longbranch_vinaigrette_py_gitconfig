import os
import pprint

from __init__ import Gitconfig

config = Gitconfig(f"{os.getcwd()}/.gitconfig")
print("Parsed gitconfig: ")
pprint.pprint(config.loads())
print("Adding some fields: ")
config.data["new_field"] = "something"

# Add a new field to every 'region'
for region in config.regions:
    print("Adding new_field to: ", region)
    config.data[region]["new_field"] = "Hello there"

print("Encoded gitconfig: ")
print(config.dumps())
