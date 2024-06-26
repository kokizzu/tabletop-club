#!/usr/bin/python3

# This script takes the .po files from Weblate, and injects the translated
# messages into the default asset pack in the form of configuration files.

import datetime
import polib
import sys

def add_config(configs, asset_path, key_index, msg, locale):
    path_split = asset_path.rsplit("/", 1)
    config_path = path_split[0] + "/config." + locale + ".cfg"
    asset_name = path_split[1]

    key = ""
    if key_index == "1":
        key = "name"
    elif key_index == "2":
        key = "desc"
    else:
        return
    
    if not config_path in configs:
        configs[config_path] = {}
    
    if not asset_name in configs[config_path]:
        configs[config_path][asset_name] = {}
    
    configs[config_path][asset_name][key] = msg

if len(sys.argv) < 2:
    sys.exit("Need a locale as an argument.")

locale = sys.argv[1]
po_file = polib.pofile(locale + ".po")

# Since zh_Hans is not recognised by Godot as a locale code, we'll rename it to
# one that is recognised so the game will read the config files like any other
# locale.
if locale == "zh_Hans":
    locale = "zh"

configs = {}
for entry in po_file.translated_entries():
    for occurrence in entry.occurrences:
        add_config(configs, occurrence[0].replace("_", " "), occurrence[1],
                entry.msgstr, locale)

for config_path in configs:
    with open(config_path, "w") as config_file:
        print(config_path)
        creation_date = datetime.datetime.now()
        creation_date_str = creation_date.strftime("%Y-%m-%d %H:%M")
        config_file.write("; Generated by inject_po.py at {}\n".format(creation_date_str))

        for asset_name in configs[config_path]:
            config_file.write("[" + asset_name + "]\n")
            for key in configs[config_path][asset_name]:
                value = configs[config_path][asset_name][key]
                value = value.replace("\"", "\\\"")
                config_file.write(key + " = \"" + value + "\"\n")
            config_file.write("\n")
