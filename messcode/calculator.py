import wx
def plus(event):
    a,b=raw_input().split(' ')
    a=int(a)
    b=int(b)
    print a+b
app=wx.App()
win=wx.Frame(None,title='calculator')
bkg=wx.Panel(win)

plusbutton=wx.Button(bkg,label='plus')
plusbutton.Bind(wx.EVT_BUTTON,plus)

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(plusbutton,proportion=0,flag=wx,LEFT,border=5)

vbox=BoxSizer(wx.VERTICAL)
vbox.Add(hox,proportion=0,flag=wx.EXPAND | wx.ALL , border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT , border=5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()
