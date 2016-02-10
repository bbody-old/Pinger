from Host import Host
class HostManager:
    def __init__(self, hosts):
        self.hosts = hosts
        """
        self.filename = filename
        f = open(self.filename, 'r')
        for line in f:
            e = unicode(line.replace("\n",""))
            self.hostList.append(e)
            self.hosts.append(Host(e))
        f.close()
        """
    def addHost(self, hostname):
        self.hosts.append(Host(hostname, hostname))
    def removeHost(self, index):
        self.hosts.remove(self.hosts[index])
    def hasHost(self, address):
        for e in self.hosts:
            if (e.getHostname().lower() == unicode(address.lower())):
                print "true"
                return True
        return False
    def getSize(self):
        return len(self.hosts)
    def checkHostUp(self, index):
        return self.hosts[index].isUp()
    def getHostname(self, index):
        return self.hosts[index].getHostname()
    def getName(self, index):
        return self.hosts[index].getName()
    def checkHostsUp(self):
        results = []
        for i in range(0, self.getSize()):
            results.append(self.checkHostUp(i))
        return results
    def checkPortUp(self, index):
        return self.hosts[index].isPortUp()
    def checkPortssUp(self):
        result = []
        for i in range(0, self.getSize()):
            result.append(self.checkVNCUp(i))
        return result
    def getHosts(self):
        return self.hosts
