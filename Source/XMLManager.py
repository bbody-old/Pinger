import xml.etree.ElementTree as ET
from Host import Host

hosts_filename = "Files/hosts.xml"

class XMLManager:
    def XMLManager(self):
        self.hosts = []
    def isValidXML(self):
        if (self.isHostListValid() & self.isPortListValid()):
            return True
        else:
            return False
    def isHostListValid(self):
        tree = ET.parse(hosts_filename)
        root = tree.getroot()
        result = []
        
        for child in root:
            address = child.get('address')
            name = child.get('name')
            #print name, address
            try:
                if (name != None):
                    result.append(Host(address, name))
                    #self.hostList.append(name)
                    
                else:
                    result.append(Host(address, address))
                    #self.hostList.append(address)
            except IndexError:
                return False
                pass
        self.hosts = result
        return True
    
    def isPortListValid(self):
        return True
    def getHostList(self):
        return self.hosts
    def writeHostList(self, hostList):
        root = ET.Element('hosts')
        for e in hostList:
            child = ET.Element('host')
            child.attrib['name'] = e.getName()
            child.attrib['address'] = e.getHostname()
            root.append(child)
        file = open(hosts_filename, 'w')

        ET.ElementTree(root).write(file)
        file.close()
        
