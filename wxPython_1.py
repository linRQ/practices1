import wx


def load(event):
    file = open(fileName.GetValue())
    contents.SetValue(file.read())
    file.close()


def save(event):
    file = open(fileName.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()


app = wx.App()
win = wx.Frame(None, title="Simple Editor", size=(410, 335))
bkg = wx.Panel(win)
loadBtn = wx.Button(win, label="Open", pos=(235, 5), size=(80, 25))
loadBtn.Bind(wx.EVT_BUTTON, load)

saveBtn = wx.Button(win, label="Save", pos=(315, 5), size=(80, 25))
saveBtn.Bind(wx.EVT_BUTTON, save)
fileName = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))
contents = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)
# loadBtn = wx.Button(bkg, label="Open")
# saveBtn = wx.Button(bkg, label="Save")
# fileName = wx.TextCtrl(bkg)
# contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
#
# hbox = wx.BoxSizer()
# hbox.Add(fileName, proportion=1, flag=wx.EXPAND)
# hbox.Add(loadBtn, flag=wx.LEFT, border=5, proportion=0)
# hbox.Add(saveBtn, proportion=0, flag=wx.LEFT, border=5)
#
# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
# vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
#
# bkg.SetSize(vbox)

win.Show()
app.MainLoop()