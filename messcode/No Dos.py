import wx
def hello(event):
    print 'Hello World!'

app=wx.App()
win=wx.Frame(None,title='Hello,wxpython')
button=wx.Button(win,label='Hello')
button.Bind(wx.EVT_BUTTON,hello)
win.Show()
app.MainLoop()
