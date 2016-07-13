#coding=utf-8
import wx
app = wx.App()
win = wx.Frame(None,title='simple Editor',size=(410,355))
loadButton = wx.Button(win,label='Open',pos=(230,5),size=(80,25))
saveButton = wx.Button(win,label='Save',pos=(315,5),size=(80,25))
filename = wx.TextCtrl(win,pos=(5,5),size=(220,25))
contents = wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
win.Show()
app.MainLoop()