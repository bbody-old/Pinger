import wx
from gui import gui
MAIN = "__main__"

def main():
    #Set up UI
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()

    # Call class that handles UI
    mainGui = gui(None, -1, "")
    app.SetTopWindow(mainGui)

    # Start
    mainGui.Show()
    app.MainLoop()
    
if __name__ == MAIN:
    main()

