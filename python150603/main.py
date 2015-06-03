__author__ = 'estel'
import wx
import cv2
import numpy
class  MyFrame(wx.Frame):


     def __init__(self):
        """

        :type self: object
        """
        wx.Frame.__init__(self, None, -1,"Image Process ")

        #test
        self.p = wx.Panel(self,size = (4000, 4000))
        self.fgs = wx.BoxSizer()

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        menu.AppendRadioItem(-1, "Standard ")
        menu.AppendRadioItem(-1, "Scientific ")
        menu.AppendRadioItem(-1, "Programmer ")
        menu.AppendSeparator()
        exit = menu.Append(-1, "Exit ")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        menuBar.Append(menu, "Menu ")

        menu = wx.Menu()#RPS
        menu.Append(5, "Roberts ")
        menu.Append(6, "Prewitt ")
        menu.Append(7, "Sobel ")
        menuBar.Append(menu, "Edge Detection ")

        menu = wx.Menu()#DEOC
        menu.Append(8, "Eroded Image ")
        menu.Append(9, "Dilated Image ")
        menu.Append(10, "Open Image ")
        menu.Append(11, "Close Image ")
        menuBar.Append(menu, "Morphology ")


        menu = wx.Menu()#OE
        menu.Append(12, "OSTU ")
        menu.Append(13, "Entropy ")
        menu.Append(14, "Manual ")
        menuBar.Append(menu, "Binaryzation ")

        menu = wx.Menu()#MMB
        menu.Append(15, "Mean Noise Reduction ")
        menu.Append(16, "Median Noise Reduction ")
        menu.Append(17, "Gaussian Noise Reduction ")
        menuBar.Append(menu, "Noise Reduction ")

        menu = wx.Menu()#DSS
        menu.Append(18, "Distance Transform ")
        menu.Append(19, "Skeleton ")
        menu.Append(20, "Skeleton Reconstruction ")
        menu.Append(21, "Morphological Reconstruction ")
        menuBar.Append(menu, "Binary Image process ")

        menu = wx.Menu()#ERG
        menu.Append(22, "Edge detection ")
        menu.Append(23, "Morphological Reconstruction ")
        menu.Append(24, "Morphological gradient ")
        menuBar.Append(menu, "Graylevel Image process ")



        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU_RANGE, self.function_order , id=5, id2=24)


     def function_order(self, event):
            index = event.GetId()   #important3
            if (index==5) or (index==6) or(index==7):

                    from RPS_file import  my_RPS_edge_detection
                    image = cv2.imread('wo.jpg',0)

                    result,word=my_RPS_edge_detection(image,(index-4))
                    cv2.imwrite("tmp1.jpg", image)
                    cv2.imwrite("tmp2.jpg", result)
                    self.ClearPanel()
                    #cv2.imshow('Original image',image)
                    #cv2.imshow(word,result)
                    #cv2.waitKey (0)
                    self.p = None
                    self.p= wx.Panel(self,size = (4000, 4000))

                    self.p.SetBackgroundColour('Write')
                    fgs = wx.BoxSizer()
                    img1 = wx.Image("tmp1.jpg", wx.BITMAP_TYPE_ANY)
                    img2 = wx.Image("tmp2.jpg", wx.BITMAP_TYPE_ANY)

                    sp1 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img1))
                    sw1=  wx.StaticText(self.p, -1, "Original Image",(100, 10))

                    sp2 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img2))
                    sw2=  wx.StaticText(self.p, -1, word,(100, 10))

                    #sp3 = []
                    #sw3 = wx.StaticText(p, -1, '',(100, 10))

                    s1=wx.BoxSizer(wx.VERTICAL)
                    s1.Add(sp1)
                    s1.Add(sw1)

                    s2=wx.BoxSizer(wx.VERTICAL)
                    s2.Add(sp2)
                    s2.Add(sw2)

                    #s3=wx.Panel(self)
                    #s3.Add(sp3)
                    #s3.Add(sw3)

                    self.fgs.Add(s1)
                    self.fgs.Add(s2,flag= wx.LEFT, border=5)
                    #fgs.Add(s3,flag= wx.LEFT, border=5)
                    self.p.SetSizerAndFit(self.fgs)


            #==================================
            elif (index==8) or (index==9) or(index==10) or(index==11):
                    dlg=wx.TextEntryDialog(None,"How many times could this function Repeat?","A Question","1")
                    if dlg.ShowModal()==wx.ID_OK:
                          response=dlg.GetValue()
                    TH=int(response)
                    from DEOC_file import my_DEOC_operations

                    image = cv2.imread('wo.jpg',0)
                    k1=numpy.array([(1,1,1), (1,9,1), (1,1,1)])
                    result,word=my_DEOC_operations(image,(index-7),k1,TH)
                    cv2.imwrite("tmp1.jpg", image)
                    cv2.imwrite("tmp2.jpg", result)
                    self.ClearPanel()
                    self.p= wx.Panel(self,size = (4000, 4000))
                    self.p.SetBackgroundColour('Write')
                    fgs = wx.BoxSizer()
                    img1 = wx.Image("tmp1.jpg", wx.BITMAP_TYPE_ANY)
                    img2 = wx.Image("tmp2.jpg", wx.BITMAP_TYPE_ANY)
                    sp1 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img1))
                    sw1=  wx.StaticText(self.p, -1, "Original Image",(100, 10))
                    sp2 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img2))
                    sw2=  wx.StaticText(self.p, -1, word,(100, 10))
                    s1=wx.BoxSizer(wx.VERTICAL)
                    s1.Add(sp1)
                    s1.Add(sw1)
                    s2=wx.BoxSizer(wx.VERTICAL)
                    s2.Add(sp2)
                    s2.Add(sw2)
                    self.fgs.Add(s1)
                    self.fgs.Add(s2,flag= wx.LEFT, border=5)
                    self.p.SetSizerAndFit(self.fgs)
            #==================================
            elif (index==12) or (index==13) or(index==14):
                    value=1
                    if  index==14:
                          dlg=wx.TextEntryDialog(None,"The grayscale you choose?(0~255)","A Question","1")
                          if dlg.ShowModal()==wx.ID_OK:
                             response=dlg.GetValue()
                          tmp=int(response)
                          if tmp>255:
                             value=255
                          elif tmp<0:
                             value=0
                          else:
                             value=tmp



                    from OE_file import  my_OE_thresholdoperation
                    image = cv2.imread('wo.jpg',0)
                    result,histogram,word=my_OE_thresholdoperation(image,(index-11),value)
                    cv2.imwrite("tmp1.jpg", image)
                    cv2.imwrite("tmp2.jpg", result)
                    cv2.imwrite("tmp3.jpg", histogram)
                    self.ClearPanel()
                    self.p= wx.Panel(self,size = (4000, 4000))
                    self.p.SetBackgroundColour('Write')
                    fgs = wx.BoxSizer()
                    img1 = wx.Image("tmp1.jpg", wx.BITMAP_TYPE_ANY)
                    img2 = wx.Image("tmp2.jpg", wx.BITMAP_TYPE_ANY)
                    img3 = wx.Image("tmp3.jpg", wx.BITMAP_TYPE_ANY)
                    sp1 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img1))
                    sw1=  wx.StaticText(self.p, -1, "Original Image",(100, 10))
                    sp2 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img2))
                    sw2=  wx.StaticText(self.p, -1, word,(100, 10))
                    sp3 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img3))
                    sw3=  wx.StaticText(self.p, -1, "histogram Image",(100, 10))
                    s1=wx.BoxSizer(wx.VERTICAL)
                    s1.Add(sp1)
                    s1.Add(sw1)

                    s2=wx.BoxSizer(wx.VERTICAL)
                    s2.Add(sp2)
                    s2.Add(sw2)

                    s3=wx.BoxSizer(wx.VERTICAL)
                    s3.Add(sp3)
                    s3.Add(sw3)

                    self.fgs.Add(s1)
                    self.fgs.Add(s2,flag= wx.LEFT, border=5)
                    self.fgs.Add(s3,flag= wx.LEFT, border=5)
                    self.p.SetSizerAndFit(self.fgs)

            elif (index==15) or (index==16) or(index==17):
                    size=3
                    value=2
                    if  index==17:
                          dlg=wx.TextEntryDialog(None,"What is the The Gaussian parameter","A Question","2")
                          if dlg.ShowModal()==wx.ID_OK:
                             response=dlg.GetValue()
                          tmp=int(response)
                          value=tmp


                    from MMB_file import  my_MMB_NoiseReduction
                    image = cv2.imread('wo.jpg',0)
                    result,word=my_MMB_NoiseReduction(image,(index-14),size,value)

                    cv2.imwrite("tmp1.jpg", image)
                    cv2.imwrite("tmp2.jpg", result)
                    self.ClearPanel()
                    self.p= wx.Panel(self,size = (4000, 4000))
                    self.p.SetBackgroundColour('Write')
                    fgs = wx.BoxSizer()
                    img1 = wx.Image("tmp1.jpg", wx.BITMAP_TYPE_ANY)
                    img2 = wx.Image("tmp2.jpg", wx.BITMAP_TYPE_ANY)
                    sp1 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img1))
                    sw1=  wx.StaticText(self.p, -1, "Original Image",(100, 10))
                    sp2 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img2))
                    sw2=  wx.StaticText(self.p, -1, word,(100, 10))
                    s1=wx.BoxSizer(wx.VERTICAL)
                    s1.Add(sp1)
                    s1.Add(sw1)
                    s2=wx.BoxSizer(wx.VERTICAL)
                    s2.Add(sp2)
                    s2.Add(sw2)
                    self.fgs.Add(s1)
                    self.fgs.Add(s2,flag= wx.LEFT, border=5)
                    self.p.SetSizerAndFit(self.fgs)

            #==================================
            elif (index==18) or (index==19) or(index==20) or(index==21):
                    from DSS_file import  my_DSS_operation
                    if index!=21:
                            image = cv2.imread('ball.bmp',0)
                            result,word=my_DSS_operation(image,(index-17))
                    else:
                            image = cv2.imread('HEAD.JPG',0)
                            result,word=my_DSS_operation(image,(index-17))

                    cv2.imwrite("tmp1.jpg", image)
                    cv2.imwrite("tmp2.jpg", result)
                    self.ClearPanel()
                    self.p = wx.Panel(self,size = (4000, 4000))
                    self.p.SetBackgroundColour('Write')
                    self.fgs = wx.BoxSizer()
                    img1 = wx.Image("tmp1.jpg", wx.BITMAP_TYPE_ANY)
                    img2 = wx.Image("tmp2.jpg", wx.BITMAP_TYPE_ANY)

                    sp1 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img1))
                    sw1=  wx.StaticText(self.p, -1, "Original Image",(100, 10))
                    sp2 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img2))
                    sw2=  wx.StaticText(self.p, -1, word,(100, 10))
                    s1=wx.BoxSizer(wx.VERTICAL)
                    s1.Add(sp1)
                    s1.Add(sw1)
                    s2=wx.BoxSizer(wx.VERTICAL)
                    s2.Add(sp2)
                    s2.Add(sw2)
                    self.fgs.Add(s1)
                    self.fgs.Add(s2,flag= wx.LEFT, border=5)
                    #self.p.SetSizerAndFit(self.fgs)
                    self.p.SetSizerAndFit(self.fgs)
            elif (index==22) or (index==23) or(index==24) :
                    thea=1
                    if  (index==22) or (index==24):
                        dlg=wx.SingleChoiceDialog(None,"What version of function are you using?",
                              "Single Choice",
                              ['Standard','External','Internal'])
                        if dlg.ShowModal()==wx.ID_OK:
                           response=dlg.GetStringSelection()
                           if response=='Standard':
                              thea=1
                           elif response=='External':
                              thea=2
                           elif response=='Internal':
                              thea=3
                    image= cv2.imread('wo.jpg',0)
                    from ERG_file import  my_ERG_operations
                    result,word=my_ERG_operations(image,(index-21),thea)


                    cv2.imwrite("tmp1.jpg", image)
                    cv2.imwrite("tmp2.jpg", result)
                    self.ClearPanel()
                    self.p= wx.Panel(self,size = (4000, 4000))
                    self.p.SetBackgroundColour('Write')
                    fgs = wx.BoxSizer()
                    img1 = wx.Image("tmp1.jpg", wx.BITMAP_TYPE_ANY)
                    img2 = wx.Image("tmp2.jpg", wx.BITMAP_TYPE_ANY)
                    sp1 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img1))
                    sw1=  wx.StaticText(self.p, -1, "Original Image",(100, 10))
                    sp2 = wx.StaticBitmap(self.p, -1, wx.BitmapFromImage(img2))
                    sw2=  wx.StaticText(self.p, -1, word,(100, 10))
                    s1=wx.BoxSizer(wx.VERTICAL)
                    s1.Add(sp1)
                    s1.Add(sw1)
                    s2=wx.BoxSizer(wx.VERTICAL)
                    s2.Add(sp2)
                    s2.Add(sw2)
                    self.fgs.Add(s1)
                    self.fgs.Add(s2,flag= wx.LEFT, border=5)
                    self.p.SetSizerAndFit(self.fgs)














            import os
            try:
                os.remove('tmp1.jpg')
                os.remove('tmp2.jpg')
                os.remove('tmp3.jpg')
            except  WindowsError:
                pass

     def OnExit(self,event):
         self.Close()

     def ClearPanel(self):
         for child in self.p.GetChildren():
                child.Destroy()




app = wx.App()
frame = MyFrame()
frame.SetSize(size=(1000,600))
frame.Show()
app.MainLoop()