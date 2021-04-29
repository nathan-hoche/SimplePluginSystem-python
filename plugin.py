import json
import sys
import os
import importlib


############ This part is for generate plugin's log
def log(func):
    try:
        fd = open("plugin.log", "w")
    except:
        fd = open("plugin.log", "x")
    old_stdout = sys.stdout
    sys.stdout = fd
    plugin_list = func()
    sys.stdout.close
    sys.stdout = old_stdout
    return plugin_list
##################################################

def load_json():
    with open("plugin/plugin.json") as f:
        data = json.load(f)
        f.close()
    return data

def load_plugin(info):
    try:
        sys.path.append(os.getcwd() + "/plugin/")
        fd = importlib.import_module(info["FileName"].replace(".py", ""))
        print("File", info["FileName"], "found.")
    except:
        print("ERROR: File", info["FileName"], "not found.")
        return None
    try:
        classfd = eval('fd.' + info["ClassName"] + '()')
        print("Class found")
        ####### Check if sample fonction is set
        classfd.edit()
        print("Edit found")
        classfd.desc()
        print("Desc found")
        classfd.update()
        print("Update found")
        #######################################
    except:
        print("ERROR: class/method crashed")
        return None
    return classfd

@log
def get_plugin():
    plugin_list = load_json()
    plugin = []
    for info in plugin_list["PLUGIN"]:
        print(info)
        if (info["activate"] == 1):
            tmp = load_plugin(info)
            if (tmp != None):
                plugin.append(tmp)
        else:
            print("INFO: module is not activate")
    return plugin

class PLUGIN:
    def __init__(self) -> None:
        self.plugin = get_plugin

    ############ Sample of plugin's fonction (server side)
    def edit(self, map):
        for plugin in self.plugin:
            map = plugin.edit(map)
        return map

    def desc(self):
        for plugin in self.plugin:
            plugin.desc()

    def update(self, map):
        for plugin in self.plugin:
            map = plugin.update(map)
        return map
    ######################################################