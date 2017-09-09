import wx
def load(event):
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file=open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()
    
def pprint(event):
    a=input()
    print'My name is matthew.'
app=wx.App()
win=wx.Frame(None,title='written by matthew')
bkg=wx.Panel(win)

pprintButton=wx.Button(bkg,label='pprint')
pprintButton.Bind(wx.EVT_BUTTON,pprint)

loadButton=wx.Button(bkg,label='Open')
loadButton.Bind(wx.EVT_BUTTON,load)

saveButton=wx.Button(bkg,label='Save')
saveButton.Bind(wx.EVT_BUTTON,save)

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(pprintButton,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM |wx.RIGHT,border=5)
bkg.SetSizer(vbox)

win.Show()
app.MainLoop()
