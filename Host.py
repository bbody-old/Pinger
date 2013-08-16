import subprocess
from socket import *
flag = '-n 1'
class Host:
    def __init__(self, address, name):
        self.address = address
        self.name = name
    def isUp(self):
        command = "ping " + flag + " " + self.address
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        response = subprocess.call(command, startupinfo=startupinfo)
        if (response == 0):
            return True
        else:
            return False
    def getHostname(self):
        return self.address
    def getName(self):
        return self.name
    def isValidIP(self):
        try:
            addr = inet_aton(self.address)
        except error:
            return False
        return self.address.count('.') == 3
    def isPortUp(self):
        result = False
        s = socket(AF_INET, SOCK_STREAM)
        if (self.isValidIP() == True):
            print "Porty" + self.address
            try:
                for i in [5800]:
                    s.settimeout(5)
                    result = s.connect_ex((gethostbyname(self.address), i))
                    print i, " Result: ", result
                    if result == 0:
                        print "Up"
                        return True
            finally:
                s.close()
        return result
