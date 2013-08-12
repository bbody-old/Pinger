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
            addr = inet_pton(AF_INET, self.address)
        except AttributeError:
            try:
                addr = inet_aton(self.address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:
            return False
        return True
    def isPortUp(self):
        result = False
        s = socket(AF_INET, SOCK_STREAM)
        if (self.isValidIP == False):
            try:
                for i in range(5900,5902):
                    s.settimeout(5)
                    result = s.connect_ex((gethostbyname(self.address), i))
                    if result == 0:
                        result = True
            finally:
                s.close()
        else:
            result
        return result
