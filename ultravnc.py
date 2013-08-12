import xml.etree.ElementTree as ET
import subprocess
from threading import Thread

config_filename = "config.xml"

class UltraVNC():
    def __init__(self):
        tree = ET.parse(config_filename)
        root = tree.getroot()
        
        for child in root:
            if child.tag == "ultravnc":
                self.program_directory = child.get("directory")
                print self.program_directory, len(self.program_directory)
    def connect(self, ip):
        if (len(self.program_directory) > 0):
            thread = Thread(target = start, args = ([ip, self.program_directory],))
            thread.start()
        
def start(arg):
    arguments = [arg[1], "-autoreconnect", "-connect", arg[0]]
    subprocess.call(arguments)
