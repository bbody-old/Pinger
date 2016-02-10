#Pinger
##Description
A small Python applicatio to track remote hosts for Windows. It also allows direct connecting to UltraVNC.

![alt text](https://s3-ap-southeast-2.amazonaws.com/bbody-images/github/Pinger/screenshot.png "Screenshot of Pinger")

## Running instructions
### Executable
Download the packaged Windows executable from [here](https://github.com/bbody/Pinger/releases). Run *Pinger.exe*.

### From Source
1. [Download Python](https://www.python.org/)
2. [Download wxPython](http://www.wxpython.org/)
3. Get source code `git clone https://github.com/bbody/Pinger.git`
4. Run `Pinger.py`

## Config files
Files already have already have example values.

### config.xml
Set UltraVNC path change `<ultravnc directory="" />` to directory of UltraVNC exe.

### ports.xml
Set ports for UltraVNC, default port is 5900.

```
<port name = "VNC">
	<number>5900</number>
</port>
```

### hosts.xml
List of hosts, requiring both an IP address or hostname with a custom name.

```
<hosts><host address="127.0.0.1" name="home" /></hosts>
```

## P2exe install
1. Download [P2exe](http://www.py2exe.org/)
2. Run command in command line `python setup.py install`

Alternatively you can download precompiled version [P2exe](https://github.com/bbody/Pinger/releases/latest)
