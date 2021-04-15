from plugin import PLUGIN
import subprocess
import time

Plugin = PLUGIN()

fd = open("map.txt", 'r')
mapr = fd.read()
fd.close()

mapr = Plugin.edit(mapr)
while(1):
    print(mapr)
    print("Description:")
    Plugin.desc()
    time.sleep(0.5)
    subprocess.run("clear")
    mapr = Plugin.update(mapr)