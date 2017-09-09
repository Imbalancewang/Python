import wx
app=wx.App()
win=wx.Frame(None,title='GUI')
bkg=wx.Panel(win)

openbutton=wx.Button(bkg,label='Open')
closebutton=wx.Button(bkg,label='Close')
savebutton=wx.Button(bkg,label='Save')

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(openbutton,proportion=0,flag=wx.LEFT,border=10)
hbox.Add(closebutton,proportion=0,flag=wx.LEFT,border=10)
hbox.Add(savebutton,proportion=0,flag=wx.LEFT,border=10)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL , border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND
         | wx.LEFT | wx.BOTTOM| wx.RIGHT ,border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
