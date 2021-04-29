import subprocess
import time

# import plugin
from plugin import PLUGIN

# Set object plugin
Plugin = PLUGIN()

###### Sample
fd = open("map.txt", 'r')
mapr = fd.read()
fd.close()

mapr = Plugin.edit(mapr) # A plugin fonction
while(1):
    print(mapr)
    print("Description:")
    Plugin.desc() # A plugin fonction
    time.sleep(2)
    subprocess.run("clear")
    mapr = Plugin.update(mapr) # A plugin fonction
#############