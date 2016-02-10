from HostManager import HostManager
from Host import Host

class HostList:
    
    def __init__(self):
        self.hosts = []
        fm = HostManager(address)
        for e in fm.getArray():
            self.hosts.append(Host(e))
    def getSize(self):
        return len(self.hosts)
    def checkHostUp(self, index):
        return self.hosts[index].isUp()
    def checkHostsUp(self):
        results = []
        for i in range(0, self.getSize()):
            results.append(self.checkHostUp(i))
        return results
    def getHostNames(self):
        results = []
        for e in self.hosts:
            results.append(e.getHostName())
        return results
